from django.urls import path
from .views import signup, signup_api, login_view, login_api, user_status_api, logout_api

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login_view'),

    path('api/signup/', signup_api, name='signup_api'),
    path('api/login/', login_api, name='login_api'),
    path('api/userstatus/', user_status_api, name='user_status_api'),
    path('api/logout/', logout_api, name='logout_api'),
]