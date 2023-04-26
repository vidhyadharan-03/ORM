from django.db import models
from django.contrib import admin
class Students (models.Model):
    Refid=models.CharField(max_length=20,help_text="student Id")
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Marks=models.IntegerField()
    Email=models.EmailField()
class StudentsAdmin(admin.ModelAdmin):
    list_display=('Refid','Name','Age','Marks','Email')