from django.db import models
from rareapi.models.user import User

class RareUser(models.Model):
    bio = models.CharField(max_length=200)
    profile_image_url = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
