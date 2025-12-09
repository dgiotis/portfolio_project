from django.shortcuts import render, redirect
from .models import Project, Skill, TimelineItem , PersonalInfo
from .forms import ContactForm
from django.urls import reverse

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all().order_by('-level')
    timeline = TimelineItem.objects.order_by('-start_year')  # newest first
    personal_info = PersonalInfo.objects.first()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home')+'?success=1')
    else:
        form = ContactForm()

    success = request.GET.get('success') == '1'

    return render(request, 'main/index.html', {
        'projects': projects,
        'skills': skills,
        'form': form,
        'success': success,
        'timeline':timeline,
        'personal_info': personal_info
    })
