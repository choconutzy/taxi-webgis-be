from django.urls import path
from rest_framework import routers


from taxi.views.taxi_views import TaxiViewSet
router = routers.DefaultRouter()
from django.urls import re_path

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taxi.views.taxi_views import TaxiViewSet
router = DefaultRouter()
router.register(r'taxi', TaxiViewSet, basename='taxi')

urlpatterns = [
    path('list/', TaxiViewSet.getAll),

]