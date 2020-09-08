from django.db import models

class Education(models.Model):
    name = models.CharField(max_length= 200)
    university = models.CharField(max_length = 200)
    university_description = models.TextField(blank = True)
    specialization = models.CharField(max_length = 200)
    graduated_year = models.IntegerField()
    competencies = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    thesis = models.CharField(max_length= 200,blank = True)
    thesis_description = models.TextField(blank = True)

class Experience(models.Model):
    name = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    starttime = models.DateField()
    endtime = models.DateField()
    description = models.TextField()
    website = models.URLField(blank = True)

class Skill(models.Model):
    skill_name = models.CharField(max_length = 100)
    items= models.TextField()
            
class Language(models.Model):
    name = models.CharField(max_length = 50)
    proficiency_choices = [('beginner','beginner'),('intermediate' 'intermediate'),('proficient', 'proficient'),('native','native')]
    proficiency = models.CharField(max_length = 20, choices = proficiency_choices)

class Extracurricular_and_hobby(models.Model):
    items = models.TextField()


    
