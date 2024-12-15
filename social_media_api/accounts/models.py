from django.contrib.auth.models import AbstractUser 
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Self-referential Many-to-Many relationship for followers and following
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username

    def follow(self, user):
        """
        Follow another user.
        """
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """
        Unfollow a user.
        """
        self.following.remove(user)

    def is_following(self, user):
        """
        Check if the current user is following another user.
        """
        return self.following.filter(pk=user.pk).exists()

    def is_followed_by(self, user):
        """
        Check if the current user is followed by another user.
        """
        return self.followers.filter(pk=user.pk).exists()
