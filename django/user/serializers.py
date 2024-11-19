from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'isstudent', 'wins', 'losses', 'creation_date', 'blocklist', 'status_2fa']