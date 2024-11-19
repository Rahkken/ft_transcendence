from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import UserRegisterForm
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json

def login(request):
    return render(request, 'user/login.html')

def signup(request):
    form = UserRegisterForm()
    return render(request, 'user/sign_up.html', {'form': form})

@require_http_methods(['POST'])
def signup_api(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

    form = UserRegisterForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({
            'message': 'Your account has been created! You are now able to log in.',
            'redirect_url': '/'
        }, status=201)
    else:
        return JsonResponse({'errors': form.errors}, status=400)