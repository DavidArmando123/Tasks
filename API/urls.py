# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserCreateView 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'tarefas', TaskViewSet)

urlpatterns = [
    path('user/', UserCreateView.as_view()), 
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
