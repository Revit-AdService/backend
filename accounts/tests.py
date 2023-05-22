from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_get_user_list(self):
        response = self.client.get('/api/accounts/users/')
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {
            'username': 'testusername',
            'email': 'test@gmail.com',
            'password': 'testpassword'
        }
        response = self.client.post('/api/accounts/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 2)
        self.assertEqual(Profile.objects.last().username, 'testusername')

    def test_get_user_detail(self):
        response = self.client.get(f'/api/accounts/users/{self.user.id}/')
        serializer = UserSerializer(self.user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        data = {
            'email': 'a@gmail.com',
        }
        response = self.client.put(f'/api/accounts/users/{self.user.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profile.objects.get(id=self.user.id).email, 'a@gmail.com')

    def test_delete_profile(self):
        response = self.client.delete(f'/api/accounts/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profile.objects.count(), 0)


class ProfileTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.profile = Profile.objects.create(
            profile_picture=None,
            phone_number='0776046899',
            address='10606 Hatcliffe',
            is_verified=True
        )

    def test_get_profile_list(self):
        response = self.client.get('/api/accounts/profiles/')
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_profile(self):
        data = {'profile_picture': '',
                'phone_number': '0776046899',
                'address': '10606 Hatcliffe',
                'is_verified': 'true'}
        response = self.client.post('/api/accounts/profiles/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 2)
        self.assertEqual(Profile.objects.last().phone_number, '0776046899')

    def test_get_profile_detail(self):
        response = self.client.get(f'/api/accounts/profiles/{self.profile.id}/')
        serializer = ProfileSerializer(self.profile)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile(self):
        data = {'phone_number': '0773851819', 'address': '2119 Bluffhill'}
        response = self.client.put(f'/api/accounts/profiles/{self.profile.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profile.objects.get(id=self.profile.id).phone_number, '0773851819')

    def test_delete_profile(self):
        response = self.client.delete(f'/api/accounts/profiles/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profile.objects.count(), 0)
