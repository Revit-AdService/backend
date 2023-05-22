from django.db import models
from django.contrib.auth.models import User
import random


class Profile(models.Model):
    """This models contains information common to the Client and the ServiceProvider"""
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=25)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'profile_{self.id}'


class Client(models.Model):
    """This model is for a User who is seeking services on the platform"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ServiceProvider(models.Model):
    """This model is for users who provide services"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20, null=True)
    id_picture = models.ImageField(upload_to='id_pictures', null=True)

    def __str__(self):
        return self.user.username


class VerificationToken(models.Model):
    identifier = models.CharField(max_length=250, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    expiry = models.DateTimeField()

    def __str__(self):
        return self.identifier

    def save(self, *args, **kwargs):
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        token = ''

        for i in range(len(characters)):
            selected = characters[random.randint(0, len(characters) - 1)]
            token += selected

        self.identifier = token
        super().save(self, *args, **kwargs)


class VerificationCode(models.Model):
    identifier = models.CharField(max_length=11, blank=True, null=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    expiry = models.DateTimeField()

    def __str__(self):
        return f'code_{self.identifier}'

    def save(self, *args, **kwargs):
        characters = '0123456789'
        code = ''

        for i in range(len(characters)):
            selected = characters[random.randint(0, len(characters) - 1)]
            code += selected

        self.identifier = code
        super().save(self, *args, **kwargs)
