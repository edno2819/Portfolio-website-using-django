from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from .models import Project, Blog, Skill, Connection, Experience, Profile
from .forms import NameForm
from django.shortcuts import render




def index(request):
    template = loader.get_template("myportfolio/index.html")
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')[:5]
    profile = Profile.objects.all().first()
    form = NameForm()
    context = {'projects': projects, 'skills': skills, 'form': form,'experiences':experiences,'profile':profile}
    return HttpResponse(template.render(context, request))


def page_cv(request):
    experiences = Experience.objects.all().order_by('-start_date')[:5]
    context = {'experiences':experiences}
    return render(request, 'myportfolio/cv.html', context)

def blog(request):
    blogs = Blog.objects.all().order_by('-published_on')
    context = {'blogs': blogs}
    return render(request, 'myportfolio/blog.html', context)

def projects(request):
    return HttpResponse("you are in projects pages")
