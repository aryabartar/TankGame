from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Cart, SoldCart

from sNeeds.apps.store.serializers import TimeSlotSaleSerializer, SoldTimeSlotSaleSerializer
from sNeeds.apps.discounts.models import TimeSlotSaleNumberDiscount
from sNeeds.apps.store.models import SoldTimeSlotSale


class CartSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="cart:cart-detail", lookup_field='id', read_only=True)
    time_slot_sales_detail = serializers.SerializerMethodField(read_only=True)
    time_slot_sales_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'url', 'user', 'time_slot_sales', 'time_slot_sales_detail',
                  'subtotal', 'time_slot_sales_dis'
                              'count', 'total', ]
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'subtotal': {'read_only': True},
            'total': {'read_only': True},
        }

    def get_time_slot_sales_discount(self, obj):
        time_slot_sale_count = obj.get_time_slot_sales_count()
        count_discount = TimeSlotSaleNumberDiscount.objects.get_discount_or_zero(time_slot_sale_count)
        return count_discount

    def get_time_slot_sales_detail(self, obj):
        return TimeSlotSaleSerializer(
            obj.time_slot_sales,
            context=self.context,
            many=True
        ).data

    def create(self, validated_data):
        user = None
        request = self.context.get('request', None)
        if request and hasattr(request, "user"):
            user = request.user

        cart_qs = Cart.objects.filter(user=user)
        if cart_qs.count() > 0:
            raise ValidationError({"detail": "User has an active cart."})

        time_slot_sales = validated_data.get('time_slot_sales', [])
        cart_obj = Cart.objects.new_cart_with_time_sales(time_slot_sales, user=user)
        return cart_obj

    def validate_time_slot_sales(self, list_of_sessions):
        sold_slots = SoldTimeSlotSale.objects.filter(sold_to=self.context.get('request').user).filter(used=False)
        for i in range(len(list_of_sessions)):
            if (sold_slots.filter(start_time__lte=list_of_sessions[i].start_time).filter(end_time__gte=list_of_sessions[i].start_time)
            or sold_slots.filter(start_time__lte=list_of_sessions[i].end_time).filter(end_time__gte=list_of_sessions[i].end_time)):
                raise ValidationError(
                    {
                        "detail": "Time Conflict between "
                                  + str(list_of_sessions[i].id) +
                                  " and "
                                  + str(sold_slots.first().id) +
                                  " which is a bought session.",
                        "detail_fa": "جلسه مشاوره  "
                                     + str(list_of_sessions[i].id) +
                                     " با "
                                     + str(sold_slots.first().id) +
                                     " که خریداری کردید؛ تداخل دارد."
                    }
                )

            for j in range(i+1, len(list_of_sessions)):
                print("j" + str(j) + "i" + str(i))
                if list_of_sessions[j].start_time <= list_of_sessions[i].start_time <= list_of_sessions[j].end_time \
                  or list_of_sessions[j].start_time <= list_of_sessions[i].start_time <= list_of_sessions[j].end_time:
                    raise ValidationError(
                        {
                            "detail": "Time Conflict between "
                                      + str(list_of_sessions[i].id)
                                      + " and " +
                                      str(list_of_sessions[j].id),
                            "detail_fa": "جلسه مشاوره  "
                                         + str(list_of_sessions[i].id) +
                                         " با "
                                         + str(list_of_sessions[j].id) +
                                         " در سبد خرید شما؛ تداخل دارد."
                        }
                    )
        return list_of_sessions


class SoldCartSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="cart:sold-cart-detail", lookup_field='id', read_only=True)
    sold_time_slot_sales_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SoldCart
        fields = [
            'id', 'url', 'user', 'sold_time_slot_sales', 'sold_time_slot_sales_detail',
            'total', 'subtotal', 'created', 'updated',
        ]

    def get_sold_time_slot_sales_detail(self, obj):
        return SoldTimeSlotSaleSerializer(
            obj.sold_time_slot_sales.all(),
            context=self.context,
            many=True
        ).data
