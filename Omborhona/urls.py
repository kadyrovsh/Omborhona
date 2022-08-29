from django.contrib import admin
from django.urls import path
from omborapp.views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="Omborhona API",
      default_version='v1',
      description="Bu loyiha Omborhona tizimini avtomatlashtirish uchun yozildi",
      contact=openapi.Contact(email="Qodirov Shukurillo. Email: <kadyrovshukurillo@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('ombor/', OmborAPIView.as_view(), name="ombor"),
    path('client/', ClientlarAPIView.as_view(), name="clientlar"),
    path('mahsulot/', MahsulotlarAPIView.as_view(), name="mahsulotlar"),
    path('stats/', StatslarAPIView.as_view(), name="statslar"),
    path('client/<int:pk>/', ClientAPIView.as_view(), name="client"),
    path('mahsulot/<int:pk>/', MahsulotAPIView.as_view(), name="mahsulot"),
    path('stats/<int:pk>/', StatsAPIView.as_view(), name="stats"),
]
