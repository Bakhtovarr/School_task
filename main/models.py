from django.db import models

# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    b_day = models.DateField()


    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    subject = models.CharField(max_length=20)
    b_day = models.DateField()


