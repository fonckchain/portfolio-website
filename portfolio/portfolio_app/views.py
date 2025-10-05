from django.shortcuts import render
from .models import Technology, Skill, Project

def home(request):
    # Get technologies grouped by category
    technologies_using = Technology.objects.filter(is_interested=False)
    technologies_interested = Technology.objects.filter(is_interested=True)

    # Get skills
    skills = Skill.objects.all()

    # Get projects (featured first)
    projects = Project.objects.all()

    context = {
        'technologies_using': technologies_using,
        'technologies_interested': technologies_interested,
        'skills': skills,
        'projects': projects,
    }

    return render(request, 'portfolio_app/home.html', context)