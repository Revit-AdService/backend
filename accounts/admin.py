from django.contrib import admin
from .models import Profile, Client, ServiceProvider, VerificationCode, VerificationToken

admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(ServiceProvider)
admin.site.register(VerificationCode)
admin.site.register(VerificationToken)
