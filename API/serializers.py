from rest_framework import serializers
from .models import Tarefa
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'],email=validated_data.get('email', ''),  password=validated_data['password'])

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'status', 'data_vencimento', 'dono']

    