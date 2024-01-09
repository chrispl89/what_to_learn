from rest_framework import routers
from django.urls import include, path
from .views import CommentsViewSet, LearnViewSet


router = routers.DefaultRouter()
router.register(r'Learn', LearnViewSet)
router.register(r'Comments', CommentsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
