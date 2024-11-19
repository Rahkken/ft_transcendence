from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isstudent = models.BooleanField(default=False)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)
    blocklist = models.ManyToManyField(User, blank=True, related_name="blocklist")
    status_2fa = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'