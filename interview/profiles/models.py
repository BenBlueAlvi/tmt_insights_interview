from django.db import models

from interview.core.behaviors import TimestampedModel, IsActiveModel

'''
Partially completed, needs migration script and authentication
'''
class UserProfile(TimestampedModel, IsActiveModel, models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    metadata = models.JSONField()

    class Meta:
        verbose_name_plural = "UserProfiles"

    def __str__(self) -> str:
        return self.username.name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_username(self):
        return self.username

    def is_authenticated(self):
        ...
