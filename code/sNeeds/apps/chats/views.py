from django.db.models import Q

from rest_framework import status, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import ChatOwnerPermission

from .models import Chat, Message
from . import serializers


class ChatListAPIView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = serializers.ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        qs = Chat.objects.get_all_user_chats(user)
        return qs


class ChatDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Chat.objects.all()
    serializer_class = serializers.ChatSerializer
    permission_classes = (ChatOwnerPermission, permissions.IsAuthenticated,)


class MessageListAPIView(generics.ListCreateAPIView):
    lookup_field = 'id'
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        chats_qs = Chat.objects.get_all_user_chats(user)
        messages_qs = Message.objects.get_chats_messages(chats_qs)
        return messages_qs


class MessageDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)