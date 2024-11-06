from django.urls import path
from . import views

app_name = 'security'

urlpatterns = [
	# path('vulnerable/', vulnerable_view, name='vulnerable'),
	# path('script/', script_view, name='script'),
	# path('script_2/', script_2_view, name='script_2'),
	# path('csrf/', csrf_view, name='csrf'),
    path('toggle-2fa/', views.toggle_2fa, name='toggle_2fa'),
]