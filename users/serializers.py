from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import Payments, User

class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class UserSerializer(ModelSerializer):

    class Meta:
         model = User
         fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user