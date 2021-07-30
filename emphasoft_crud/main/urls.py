from django.urls import path
from .views import *


urlpatterns = [
    path('', start_view),
]