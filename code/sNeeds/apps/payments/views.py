from zeep import Client

from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

from django.conf import settings

from rest_framework import status, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from sNeeds.apps.orders.models import Order

from .serializers import ConsultantDepositInfoSerializer
from .permissions import IsConsultant, ConsultantDepositInfoOwner
from .models import ConsultantDepositInfo
from sNeeds.apps.consultants.models import ConsultantProfile

from .models import PayPayment
from ..carts.models import Cart
from ..notifications.tasks import send_email_notifications
from ..storePackages.models import SoldStorePackagePhaseDetail
from ...settings.config.variables import FRONTEND_URL

ZARINPAL_MERCHANT = settings.ZARINPAL_MERCHANT


class SendRequest(APIView):
    """
    POST:
    {
        "cartid":12
    }
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')

        user = request.user

        try:
            cart_id = request.data.get("cartid")
            if cart_id is None:
                return Response({"detail": "cartid field is empty."}, 400)

            cart = Cart.objects.get(id=cart_id)

        except Cart.DoesNotExist:
            return Response({"detail": "No cart exists."}, 400)

        if not cart.user == user:
            return Response({"detail": "This user is not cart's owner."}, 400)

        if not cart.is_acceptable_for_pay():
            # If price is zero it may a 100 percent for one time slot. so we check that is just one time slot
            if cart.products.all().count() == 1 and cart.get_time_slot_sales_count() == 1:
                Order.objects.sell_cart_create_order(cart)
                return Response({"detail": "Success", "ReflD": "00000000"}, status=200)
            else:
                return Response({"detail": "Can not pay, The price is 0."}, 400)

        result = client.service.PaymentRequest(
            ZARINPAL_MERCHANT,
            int(cart.total),
            "پرداخت اسنیدز",
            cart.user.email,
            cart.user.phone_number,
            FRONTEND_URL + "user/payment/accept/",
        )

        if result.Status != 100:
            return Response({"detail": 'Error code: ' + str(result.Status)}, 400)

        PayPayment.objects.create(user=user, cart=cart, authority=result.Authority)

        return Response({"redirect": 'https://www.zarinpal.com/pg/StartPay/' + str(result.Authority)})


class Verify(APIView):
    """
    POST:
    {
       "authority":"000000000000000000000000000150139347",
       "status":"OK"
    }

    """
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')

        data = request.data
        if data.get('status') == 'OK':
            user = request.user
            authority = data.get('authority', None)

            try:
                payment = PayPayment.objects.get(
                    user=user,
                    authority=authority
                )

            except PayPayment.DoesNotExist:
                return Response({"detail": "PayPayment does not exists."}, status=400)

            result = client.service.PaymentVerification(ZARINPAL_MERCHANT, authority, int(payment.cart.total))

            if result.Status == 100:
                order = Order.objects.sell_cart_create_order(payment.cart)
                # TODO RefID does not save in relative order or in payment ???
                return Response(
                    {"detail": "Success",
                     "ReflD": str(result.RefID),
                     "order": order.id},
                    status=200
                )
            elif result.Status == 101:
                return Response({"detail": "Transaction submitted", "status": str(result.Status)}, status=200)
            else:
                return Response({"detail": "Transaction failed", "status": str(result.Status)}, status=400)

        else:
            return Response({"detail": "Transaction failed or canceled by user"}, status=400)


class VerifyTest(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("cartid")
        cart = Cart.objects.get(id=id)
        Order.objects.sell_cart_create_order(cart)
        return Response()


class ConsultantDepositInfoListAPIView(generics.ListAPIView):
    serializer_class = ConsultantDepositInfoSerializer
    permission_classes = [permissions.IsAuthenticated, IsConsultant]

    def get_queryset(self):
        user = self.request.user
        consultant_profile = ConsultantProfile.objects.get(user=user)
        qs = ConsultantDepositInfo.objects.filter(consultant=consultant_profile)
        return qs


class ConsultantDepositInfoDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'consultant_deposit_info_id'
    queryset = qs = ConsultantDepositInfo.objects.all()
    serializer_class = ConsultantDepositInfoSerializer
    permission_classes = [permissions.IsAuthenticated, IsConsultant, ConsultantDepositInfoOwner]

