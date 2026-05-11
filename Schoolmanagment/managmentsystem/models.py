
# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    image = models.ImageField(upload_to='students/')
    roll_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"