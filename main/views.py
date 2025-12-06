from django.shortcuts import render, redirect
from .models import Project, Skill, TimelineItem
from .forms import ContactForm
from django.urls import reverse

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    timeline = TimelineItem.objects.order_by('-start_year')  # newest first

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
        'timeline':timeline
    })
