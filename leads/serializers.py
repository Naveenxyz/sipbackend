from rest_framework import serializers
from leads.models import Lead, model_user, model_form, model_chat_thread


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = model_user
        fields = '__all__'


class form_serializer(serializers.ModelSerializer):
    class Meta:
        model = model_form
        fields = '__all__'


class model_chat_serializer(serializers.Serializer):
    class Meta:
        model = model_chat_thread
        fields = '__all__'
