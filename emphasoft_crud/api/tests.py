from rest_framework.test import APITestCase
from django.db import connection
from .models import *


class TestNoteListAPIView(APITestCase):
    def test_missing_categories(self):
        self.categories_news = Category.objects.create(title='news')
        self.notes_news = Note.objects.create(
            text='the text of the first note',
            category=self.categories_news,

        )