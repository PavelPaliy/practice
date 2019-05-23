from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    description = models.CharField(max_length=350, db_index=True)
    def __str__(self):
        return self.title



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
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username