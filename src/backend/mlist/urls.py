from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MListViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'mlists', MListViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]