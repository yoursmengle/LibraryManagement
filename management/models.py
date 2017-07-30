from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)
    mobile = models.CharField(max_length=16)
    weichat = models.CharField(max_length=128)
    alipay = models.CharField(max_lengthy=128)

    def __unicode__(self):
        return self.user.username

class Question(models.Model):
    user = models.ForeignKey(MyUser)
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=4096)
    image = models.ImageField()
    start_time = models.DateField()
    end_time = models.DateField()

class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(MyUser)
    content = models.TextField(max_length=4096)
    image = models.ImageField()
    time = models.DateField()
    place = models.IntegerField()

class Compare(models.Model):
    user = models.ForeignKey(MyUser)
    answerA = models.ForeignKey(Answer)
    answerB = models.ForeignKey(Answer)
    AisBetter = models.BoolField()
    BisBetter = models.BoolField()
    DontSure = models.BoolField()

class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    author = models.CharField(max_length=128)
    publish_date = models.DateField()
    category = models.CharField(max_length=128)

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='image/%Y/%m/%d/')
    book = models.ForeignKey(Book)

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name
