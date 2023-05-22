from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ProfileViewSet, ClientViewSet, ServiceProviderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'service-providers', ServiceProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/retrieve-client-by-user-id/<int:user_id>/',
         ClientViewSet.as_view({'get': 'retrieve_client_by_user_id'})),
    path('clients/retrieve-service-provider-by-user-id/<int:user_id>/',
         ServiceProviderViewSet.as_view({'get': 'retrieve_service_provider_by_user_id'})),
    path('verification/send-verification-email/<int:user_id>/',
         UserViewSet.as_view({'post': 'send_verification_email'})),
    path('verification/send-verification-text-message/<int:profile_id>/',
         ProfileViewSet.as_view({'post': 'send_verification_text_message'})),
    path('verification/<int:user_id>/verify-email/<str:verification_token>/',
         UserViewSet.as_view({'post': 'verify_email'})),
    path('verification/<int:profile_id>/verify-text-message/<int:verification_code>/',
         ProfileViewSet.as_view({'post': 'verify_text_message'})),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
