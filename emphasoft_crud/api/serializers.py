from rest_framework import serializers
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