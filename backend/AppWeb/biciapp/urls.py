from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views, api

router = DefaultRouter()
router.register(r'notifications', api.NotificationViewSet, 'notifications')
router.register(r'stores', api.StoreViewSet, 'stores')
urlpatterns = [
    path('', views.index, name='index'),
]

# Create your views here.
