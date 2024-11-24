from django.urls import path
from .views import signup, signup_api, login_view, login_api, user_status_api, logout_api, edit_profile_view, get_profile_api, update_profile_api

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login_view'),
    path('edit_profile/', edit_profile_view, name='edit_profile_vieww'),

    path('api/signup/', signup_api, name='signup_api'),
    path('api/login/', login_api, name='login_api'),
    path('api/userstatus/', user_status_api, name='user_status_api'),
    path('api/logout/', logout_api, name='logout_api'),
    path('api/profile/', get_profile_api, name='get_profile_api'),
    path('api/profile/update/', update_profile_api, name='update_profile_api'),
]