from django.urls import path
from home.views import welcome, welcome_partial, leaderboard, leaderboard_api, lobby, tournaments, chat, profile, profile_api

app_name = 'home'

urlpatterns = [
	path('', welcome, name='welcome'),
	path('welcome_partial/', welcome_partial, name='welcome_partial'),
	path('leaderboard/', leaderboard, name='leaderboard'),
    path('lobby/', lobby, name='lobby'),
    path('tournaments/', tournaments, name='tournaments'),
    path('chat/', chat, name='chat'),
    path('profile/', profile, name='profile'),

    path('api/leaderboard/', leaderboard_api, name='leaderboard_api'),
    # path('api/lobby/', lobby_api, name='lobby_api'),
    path('api/profile/<str:username>/', profile_api, name='profile_api'),
]