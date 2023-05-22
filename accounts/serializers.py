from rest_framework import serializers
from .models import Profile, Client, ServiceProvider
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = Client
        fields = '__all__'


class ServiceProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = ServiceProvider
        fields = '__all__'
