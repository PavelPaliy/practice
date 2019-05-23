from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
from django.http import HttpResponse
from time import time
from django.utils.text import slugify
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

def index(request):
    return render(request, 'meeting/index.html')

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


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

