from django.shortcuts import render
from .models import Project , Skill, ContactMessage

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    messages = ContactMessage.objects.all()
    return render(request, 'main/index.html', {'projects': projects, 'skills': skills, 'messages': messages,})
