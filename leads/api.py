from leads.models import Lead, model_user, model_form, model_chat_thread
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, user_serializer, form_serializer, model_chat_serializer

# lead viewset


class LeadViewsets(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer


class userviewsets(viewsets.ModelViewSet):
    queryset = model_user.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = user_serializer


class formviewsets(viewsets.ModelViewSet):
    queryset = model_form.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = form_serializer


class chatviewsets(viewsets.ModelViewSet):
    queryset = model_chat_thread.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = model_chat_serializer
