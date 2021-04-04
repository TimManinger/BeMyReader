import os
from django.db import models
from django.conf import settings

"""
class Content(models.Model):
    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

    requester = models.CharField(max_length=10)
    creator = models.CharField(max_length=10)
    # For requestor should we use django-phonenumber-field?
    head = models.TextField()
    body = models.TextField()
    idx = models.PositiveSmallIntegerField(null=True, unique=True)
"""
"""
class User(models.Model):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
	# user entered
    name = models.CharField("name", max_length=30, null=True)
    passcode = models.CharField("passcode", max_length=6, null=True)
	# grab from twilio any time someone connects
    number = models.CharField("phone number", max_length=15)
"""

class Title(models.Model):
    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'
    GENRES = [
        ('SC', 'Science'),
        ('HI', 'History'),
        ('LI', 'Literature'),
        ('MA', 'Math'),
        ('BI', 'Biography'),
        ('RE', 'Reference'),
    ]
	# user entered
    name = models.CharField("book title", max_length=50, null=True)
    author = models.CharField("book author", max_length=50, null=True)
    # reader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    genre = models.CharField("genre", max_length=2, choices=GENRES, null=True)
	# auto generated
	# id is auto generated for all models, I'm just using it for filepath
    files = models.FilePathField(null=True)
