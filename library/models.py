from django.db import models
from students.models import Student
from books.models import Book

class Library(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return f"{self.student_name} borrowed {self.book_name}"