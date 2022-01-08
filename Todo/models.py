from django.db import models
from django.db.models.enums import Choices
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class list(models.Model):
    #t = timezone.now()
    item = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='Upcoming')
    complete = models.BooleanField(default=False)
    assign_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField("due_date")

    def __str__(self) -> str:
        return self.item


class DashBoard(models.Model):
    dashBoards = [
        ('NEWTASK', 'Newtask'),
        ('PENDING', 'Pending'),
        ('COMPLETE', 'Complete'),
        ('RUNNING', 'Running'),
        ('UNKNOWN', 'Unknown')
    ]
    task = models.ForeignKey(list, on_delete=models.CASCADE)
    board = models.CharField(
        max_length=20, choices=dashBoards, default='NEWTASK')

    def __str__(self):
        return self.task


class User(AbstractUser):
    photo = models.ImageField(upload_to='media', default='media/default.png')
    token = models.CharField(null=True, max_length=50)
    token_time = models.DateTimeField(null=True)
    token_check = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name
