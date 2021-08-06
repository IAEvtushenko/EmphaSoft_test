from django.urls import path
from .views import *


urlpatterns = [
    path('create/', NoteCreateView.as_view()),
    path('my_notes/', NoteListView.as_view()),
    path('note/<int:pk>', NoteDetailView.as_view()),
    path('note/<int:pk>', NoteDetailView.as_view()),
]

