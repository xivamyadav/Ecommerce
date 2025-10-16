from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

#roter setup
router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
