from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TodoItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
