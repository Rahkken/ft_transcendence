from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import UserRegisterForm
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
import json

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

def login_view(request):
    form = AuthenticationForm
    return render(request, 'user/login.html', {'form': form})

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import random
from django.conf import settings

@require_http_methods(['POST'])
def login_api(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

    form = AuthenticationForm(request=request, data=data)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return JsonResponse({'message': 'Logged in successfully.', 'redirect_url': '/'}, status=200)
        # if user.profile.status_2fa:
        #     otp = random.randint(100000, 999999)
        #     request.session['otp'] = otp
        #     request.session['user_id'] = user.id

        #     # Send OTP via email (implement your email logic here)
        #     try:
        #         message = Mail(
        #             from_email=settings.SENDGRID_EMAIL,
        #             to_emails=user.email,
        #             subject='Your OTP Code',
        #             html_content=f'<strong>Your OTP code is {otp}</strong>'
        #         )
        #         sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        #         sg.send(message)
        #     except Exception as e:
        #         return JsonResponse({'error': f'Failed to send OTP email: {e}'}, status=500)

        #     return JsonResponse({'message': 'OTP sent. Please verify.', 'redirect_url': '/verify-otp/'}, status=200)
        # else:
        #     login(request, user)  # Log the user in
        #     return JsonResponse({'message': 'Logged in successfully.', 'redirect_url': '/'}, status=200)
    else:
        errors = form.errors.as_json()
        return JsonResponse({'errors': json.loads(errors)}, status=400)

@require_http_methods(['GET'])
def user_status_api(request):
    if request.user.is_authenticated:
        return JsonResponse({'is_logged_in': True, 'username': request.user.username})
    return JsonResponse({'is_logged_in': False})

@require_http_methods(['POST'])
def logout_api(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'message': 'Successfully logged out.', 'redirect_url': '/'}, status=200)
    else:
        return JsonResponse({'error': 'You are not logged in.'}, status=400)

from .models import Profile
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required

def edit_profile_view(request):
    return render(request, 'user/edit_profile.html')

@login_required(login_url='/?redirected=true')
@require_http_methods(["GET"])
def get_profile_api(request):
    """Retrieve the current user's profile as JSON."""
    user = request.user
    profile = Profile.objects.get(user=user)
    
    data = {
        'username': user.username,
        'email': user.email,
        'wins': profile.wins,
        'losses': profile.losses,
    }
    return JsonResponse(data, status=200)

def update_profile_api(request):
    """Update the current user's profile using the provided forms."""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            return JsonResponse({'message': 'Profile updated successfully'}, status=200)
        else:
            errors = {
                'user_errors': u_form.errors,
            }
            return JsonResponse({'errors': errors}, status=400)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)