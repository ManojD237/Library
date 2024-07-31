from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.student_name
