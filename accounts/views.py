from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .models import Profile, Client, ServiceProvider
from .serializers import UserSerializer, ProfileSerializer, ClientSerializer, ServiceProviderSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=data['username'])
            user.set_password(data['password'])
            user.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def send_verification_email(self, request, *args, **kwargs):
        pass

    @action(methods=['post'], detail=False)
    def verify_email(self, request):
        pass


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = []
    permission_classes = []

    @action(methods=['post'], detail=False)
    def send_verification_text_message(self, request, *args, **kwargs):
        pass

    @action(methods=['post'], detail=False)
    def verify_text_message(self, request):
        pass


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = []
    permission_classes = []

    @action(methods=['get'], detail=False)
    def retrieve_client_by_user_id(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs['user_id'])
        except User.DoesNotExist:
            return Response(data={'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                client = Client.objects.get(user=user)
            except Client.DoesNotExist:
                return Response(data={'message': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                serialized_data = ClientSerializer(client).data
                return Response(serialized_data, status=status.HTTP_200_OK)


class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    authentication_classes = []
    permission_classes = []

    @action(methods=['get'], detail=False)
    def retrieve_service_provider_by_user_id(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs['user_id'])
        except User.DoesNotExist:
            return Response(data={'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                client = ServiceProvider.objects.get(user=user)
            except ServiceProvider.DoesNotExist:
                return Response(data={'message': 'Service provider not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                serialized_data = ServiceProviderSerializer(client).data
                return Response(serialized_data, status=status.HTTP_200_OK)
