from django.db import models
import datetime
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    description =models.TextField(blank=True, db_index=True)
    on_vote = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('meeting_detail_url', kwargs={'slug': self.slug})



class MeetingDate(models.Model):
    date = models.DateTimeField()
    status = models.BooleanField(default=0)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    number_of_votes = models.IntegerField(default=0)

class Vote(models.Model):
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, primary_key=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username