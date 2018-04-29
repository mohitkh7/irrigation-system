"""
API urls
"""
from django.urls import path, include

from .views_api import create_status, read_instruction, last_status, all_status, update_mode, update_set

urlpatterns = [
    path('create/', create_status, name='create'),
    path('last/', last_status, name='last'),
    path('all/',all_status, name="all"),
    path('read/', read_instruction, name="read"),

    path('update-mode/',update_mode, name="update-mode"),
    path('update-set/',update_set, name="update-set"),
]
