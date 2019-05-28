from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
from django.http import HttpResponse
from time import time
from django.utils.text import slugify
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import View

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

def index(request):
    if request.user.is_authenticated:
        meetings = Meeting.objects.all()
        return render(request, 'meeting/index.html', context={'meetings':meetings})
    else:
        return redirect('login')

def create(request):
    form_model_date = MeetingDateForm
    form_meeting = MeetingForm
    form_vote = VoteForm
    return render(request, 'meeting/meeting_create.html', context={'form_date':form_model_date, 'form_meeting': form_meeting, 'form_vote':form_vote})

def result(request):
    res = request.POST
    meeting = Meeting(title = res.get('title'), slug = gen_slug(res.get('title')), description = res.get('description'))
    meeting.save()
    index = 1
    while res.get(str(index)+'date'):
        date = MeetingDate(date = res.get(str(index)+'date'), status = False, meeting = meeting)
        date.save()
        index = index + 1
    vote = Vote(meeting=meeting, start = res.get('start'), end = res.get('end'))
    vote.save()
    return redirect('vote_detail_url', slug = meeting.slug)



def voteDetail(request, slug):
    meeting = Meeting.objects.get(slug__iexact=slug)
    vote = meeting.vote
    dates = MeetingDate.objects.filter(meeting=meeting)
    return render(request, 'meeting/vote_detail.html', context={'vote':vote, 'dates': dates})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index_url'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'meeting/login.html', {})


def register(request):
  registered = False
  if request.method == 'POST':
      user_form = UserForm(data=request.POST)

      if user_form.is_valid():
          user = user_form.save()
          user.set_password(user.password)
          user.save()
          registered = True

      else:
          print(user_form.errors)
  else:
      user_form = UserForm()
  return render(request,'meeting/registration.html',
                        {'user_form':user_form,
                          'registered':registered})