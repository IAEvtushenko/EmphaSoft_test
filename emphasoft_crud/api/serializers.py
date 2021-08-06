from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


#Описание передачи конкретной записи

class NoteDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Note
        fields = '__all__'


#Описание передачи списка записей пользователя

class NoteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'text',)


class RetrieveUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class UpdateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password')
        employee = Employee(**validated_data)
        employee.set_password(password)
        employee.save()
        return employee

    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name', 'department', 'salary', 'current_project', 'password', 'is_active',)