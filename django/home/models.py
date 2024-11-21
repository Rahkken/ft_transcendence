from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Party(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    num_players = models.IntegerField(choices=[(0, 'Play Local'), (1, 'Play with AI'), (2, '2 Players'), (3, '3 Players')], default=2)
    nbPlayer = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
        default='active'
    )
    participants = models.ManyToManyField(User, related_name='parties_joined', blank=True) 

    def __str__(self):
        return f"Party {self.id} by {self.creator.username}"

    class Meta:
        db_table = 'game_party'

class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username
    
    def add_friend(self, account):
        """
        Add a new friend
        """
        if account not in self.friends.all():
            self.friends.add(account)
            self.save()
    
    def remove_friend(self, account):
        """
        Remove friend
        """
        if account in self.friends.all():
            self.friends.remove(account)
    
    def unfriend(self, target):
        """
        Unfriend someone
        """
        my_friends_list = self # person terminating 
        my_friends_list.remove_friend(target)

        targets_friends_list = FriendList.objects.get(user=target)
        targets_friends_list.remove_friend(self.user)

    def is_mutual_friend(self, target):
        """
        Is this a friend
        """
        if target in self.friends.all():
            return True
        return False

class FriendRequest(models.Model):
    """
    A friend request consists of two main parts:
        1. SENDER:
            - Person sending the friend request
        2. RECEIVER:
            - Person receiving the friend request
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username
    
    def accept(self):
        """
        Accept a friend request
            Update both SENDER and RECEIVER friend lists
        """
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()
    
    def decline(self):
        """
        Decline a friend request (sent to you)
            Is it "declined" by setting the "is_active" field to False
        """
        self.is_active = False
        self.save()
    
    def cancel(self):
        """
        Cancel a friend request (you sent)
            It is "cancelled" by setting the "is_active" field to False
        """
        self.is_active = False
        self.save()

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    opponent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='opponent_entries', null=True, blank=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    player_score = models.IntegerField()
    opponent_score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        opponent_username = self.opponent.username if self.opponent else 'Unknown'
        return f"{self.user.username} vs {opponent_username} - {self.player_score} vs {self.opponent_score} at {self.timestamp}"