from django.urls import path
from base.views import banner_views as views


urlpatterns = [
    path('', views.getBanners, name="banners"),
]