# Django
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator

User: AbstractBaseUser = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    sm_pp = models.SmallIntegerField(validators=[MaxValueValidator(5)])


class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()
    authors = models.ManyToManyField(to=Author, related_name='books')
