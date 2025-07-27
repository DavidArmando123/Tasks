# views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Tarefa
from .serializers import TaskSerializer, UserRegisterSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]  

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        return Tarefa.objects.filter(dono=self.request.user)

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)
