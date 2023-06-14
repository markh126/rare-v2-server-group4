from django.db import models
from .rareuser import RareUser
from .post import Post


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_id = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name = 'comments')
    content = models.CharField(max_length=280)
    created_on = models.DateField()
