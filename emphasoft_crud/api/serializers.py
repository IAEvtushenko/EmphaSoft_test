from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


User = get_user_model()


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
        model = User
        fields = '__all__'


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'is_active',)