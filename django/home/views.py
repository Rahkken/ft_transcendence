from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from user.models import Profile
from django.http import JsonResponse

# Create your views here.

def welcome(request):
	return render(request, 'home/welcome.html')

def welcome_partial(request):
	return render(request, 'home/welcome_partial.html')

def leaderboard(request):
	return render(request, 'home/leaderboard.html')

@require_http_methods(['GET'])
def leaderboard_api(request):
    profiles = Profile.objects.all().order_by('-wins')

    leaderboard_data = []
    for profile in profiles:
        leaderboard_data.append({
            'username': profile.user.username,
            'wins': profile.wins,
            'losses': profile.losses,
        })

    return JsonResponse({'leaderboard': leaderboard_data})

def lobby(request):
	return render(request, 'home/lobby.html')

def tournaments(request):
	return render(request, 'home/tournaments.html')

def chat(request):
	return render(request, 'home/chat.html')

def profile(request):
	return render(request, 'home/profile.html')

# from django.http import JsonResponse
# from django.core.serializers import serialize
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_http_methods
# from .forms import CreatePartyForm
# from .models import Party
# import json

# @csrf_exempt
# @require_http_methods(["GET", "POST"])
# def lobby_api(request):
#     if request.method == 'POST':
#         # Parse JSON data from the request
#         try:
#             data = json.loads(request.body)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

#         form = CreatePartyForm(data)
#         num_players = data.get('num_players', None)

#         # Ensure num_players is an integer
#         try:
#             num_players = int(num_players)
#         except (ValueError, TypeError):
#             return JsonResponse({'error': 'num_players must be a valid integer'}, status=400)

#         # Handle cases based on num_players
#         if num_players == 1:
#             return JsonResponse({
#                 'party_id': None,
#                 'match_id': None,
#                 'tournament_id': None,
#                 'user': request.user.username,
#                 'num_players': 1,
#             })
#         elif num_players == 0:
#             return JsonResponse({
#                 'party_id': None,
#                 'match_id': None,
#                 'tournament_id': None,
#                 'user': request.user.username,
#                 'num_players': 0,
#             })

#         # Validate and save the form
#         if form.is_valid():
#             party = form.save(commit=False)
#             party.creator = request.user
#             party.save()
#             return JsonResponse({'message': 'Party created successfully', 'party_id': party.id}, status=201)
#         else:
#             return JsonResponse({'errors': form.errors}, status=400)

#     else:  # Handle GET request
#         parties = Party.objects.exclude(status='completed')
#         parties_data = [
#             {
#                 'id': party.id,
#                 'name': party.name,
#                 'creator': party.creator.username,
#                 'status': party.status,
#                 'num_players': party.num_players,
#             }
#             for party in parties
#         ]

#         return JsonResponse({
#             'parties': parties_data,
#             'num_players': None  # Default for GET requests
#         }, status=200)