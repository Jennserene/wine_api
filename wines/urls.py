# wines/urls.py
from django.urls import path, include
# This library gives us all of the functions usually found in views.py
from .views import WineViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', WineViewSet, basename='wine')
urlpatterns = router.urls
