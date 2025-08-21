from django.urls import path
from . import views
from .views import MenuAPIView, BookingAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('api/menu/', MenuAPIView.as_view(), name='menu-api'),
    path('api/booking/', BookingAPIView.as_view(), name='booking-api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
