from django.db import models
from .rare_user import RareUser

class Post(models.Model):
    
    user_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='user',default=1)
    
    title = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    image_url = models.CharField(max_length=255)
    content = models.TextField()
  
