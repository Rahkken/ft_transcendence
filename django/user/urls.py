from django.urls import path
from .views import signup, signup_api, login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),

    path('api/signup/', signup_api, name='signup_api'),
]