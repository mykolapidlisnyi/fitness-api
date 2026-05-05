from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, WorkoutViewSet, TrainerViewSet, HealthProfileViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'health-profiles', HealthProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]