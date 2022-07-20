from turtle import title
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    publishYear = models.DecimalField(max_digits=5, decimal_places=0)
    createdTime = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id', 'title', 'author','publsihYear']

    def __str__(self):
        return self.title