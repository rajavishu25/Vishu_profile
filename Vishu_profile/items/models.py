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

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    starttime = models.DateField()
    endtime = models.DateField()
    description = models.TextField()
    website = models.URLField(blank = True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    skill_name = models.CharField(max_length = 100)
    items= models.TextField()

    def __str__(self):
        return self.skill_name
            
class Language(models.Model):
    name = models.CharField(max_length = 50)
    proficiency_choices = [('1','beginner'),('2','intermediate'),('3', 'proficient'),('4','native')]
    proficiency = models.CharField(max_length = 20, choices = proficiency_choices)

    def __str__(self):
        return self.name

class Extracurricular_and_hobby(models.Model):
    items = models.TextField()

    def __str__(self):
        return "Extra curricular activities and Hobbies"


    
