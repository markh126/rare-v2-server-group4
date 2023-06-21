from django.db import models

class RareUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    profile_image_url = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    uid = models.CharField(max_length=200)
