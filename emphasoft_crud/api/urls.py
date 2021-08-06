from django.urls import path
from .views import *


urlpatterns = [
    path('create/notes/', NoteCreateView.as_view()),
    path('notes/', NoteListView.as_view()),
    path('notes/<int:pk>/', NoteDetailView.as_view()),
    path('create_user/', UserCreateView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
]

