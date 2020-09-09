from django.shortcuts import render
from .models import Education,Experience, Skill, Extracurricular_and_hobby, Language

def home(request):
    return render(request,'home.html')

