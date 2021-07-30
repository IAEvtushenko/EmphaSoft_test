import json

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название категории')

    def __str__(self):
        return self.title


class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    text = models.TextField(verbose_name='Запись')
    date = models.DateTimeField(verbose_name='Дата изменения', default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text