from django.shortcuts import render
from .models import Education,Experience, Skill, Extracurricular_and_hobby, Language

def home(request):
    return render(request,'home.html')

def education(request):
    education = Education.objects.all
    return render(request,'education.html',{'education': education })

def experience(request):
    experience = Experience.objects.all
    return render(request, 'experience.html', {'experience' : experience})

def skills(request):
    skills = Skill.objects.all
    languages = Language.objects.all
    return render(request, 'skills.html', {'skills' : skills, 'languages': languages})

def hobbies(request):
    hobbies = Extracurricular_and_hobby.objects.all
    return render(request, 'hobbies.html', {'hobbies' : hobbies})


