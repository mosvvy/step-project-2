from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='search')

    city = models.CharField(max_length=100)
    result = models.JSONField()

    def __str__(self):
        return self.city
