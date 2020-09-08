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
    
