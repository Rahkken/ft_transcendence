from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from user.models import Profile
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import FriendList, LeaderboardEntry, FriendRequest
from .utils import get_friend_request_or_false, FriendRequestStatus
# from .forms import CreatePartyForm
# from .models import Party
# import json

# Create your views here.

def welcome(request):
	return render(request, 'home/welcome.html')

def welcome_partial(request):
	return render(request, 'home/welcome_partial.html')

@login_required(login_url='/?redirected=true')
def leaderboard(request):
	return render(request, 'home/leaderboard.html')

@login_required(login_url='/?redirected=true')
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

@login_required(login_url='/?redirected=true')
def lobby(request):
    return render(request, 'home/lobby.html')

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

@login_required(login_url='/?redirected=true')
def tournaments(request):
	return render(request, 'home/tournaments.html')

@login_required(login_url='/?redirected=true')
def chat(request):
	return render(request, 'home/chat.html')

@login_required(login_url='/?redirected=true')
def profile(request):
	return render(request, 'home/profile.html')

@login_required(login_url='/?redirected=true')
@require_http_methods(["GET"])
def profile_api(request, username):
    try:
        displayed_user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    profile_data = {
        'username': displayed_user.username,
        'id': displayed_user.id,
        'email': displayed_user.email,
        'wins': displayed_user.profile.wins,
        'losses': displayed_user.profile.losses,
        'blocklist': [user.username for user in displayed_user.profile.blocklist.all()],
    }

    try:
        friend_list = FriendList.objects.get(user=displayed_user)
    except FriendList.DoesNotExist:
        friend_list = FriendList(user=displayed_user)
        friend_list.save()
    profile_data['friends'] = [friend.username for friend in friend_list.friends.all()]

    latest_matches = LeaderboardEntry.objects.filter(user=displayed_user).order_by('-timestamp')[:10]
    profile_data['latest_matches'] = [
        {'opponent': match.opponent.username, 'score': match.score, 'timestamp': match.timestamp}
        for match in latest_matches
    ]

    is_self = True
    is_friend = False
    request_sent = FriendRequestStatus.NO_REQUEST_SENT.value
    friend_requests = None
    user = request.user

    if user.is_authenticated and user != displayed_user:
        is_self = False
        if friend_list.friends.filter(pk=user.id).exists():
            is_friend = True
        else:
            if get_friend_request_or_false(sender=displayed_user, receiver=user):
                request_sent = FriendRequestStatus.THEM_SENT_TO_YOU.value
            elif get_friend_request_or_false(sender=user, receiver=displayed_user):
                request_sent = FriendRequestStatus.YOU_SENT_TO_THEM.value

    elif not user.is_authenticated:
        is_self = False
    else:
        friend_requests = FriendRequest.objects.filter(receiver=user, is_active=True)

    profile_data.update({
        "is_self": is_self,
        "is_friend": is_friend,
        "request_sent": request_sent,
        "friend_requests": [
            {"id": fr.id, "sender": fr.sender.username} for fr in friend_requests
        ] if friend_requests else [],
    })

    return JsonResponse(profile_data, status=200)