from django.db import models
from .rare_user import RareUser
from datetime import date

class Subscription(models.Model):
    follower_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='follower')
    author_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='author')
    created_on = models.DateField(auto_now_add=True)
    ended_on = models.DateField(null=True)
