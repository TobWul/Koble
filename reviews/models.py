from django.db import models

from authentication.models import Profile


class Review(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)