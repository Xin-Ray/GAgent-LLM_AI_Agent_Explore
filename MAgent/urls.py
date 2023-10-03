from django.urls import path
from .views import game_view

app_name = "MAgent"
urlpatterns = [
    path('game/', game_view, name='game_view'),
]
