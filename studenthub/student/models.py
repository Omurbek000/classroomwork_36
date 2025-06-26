from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
      return self.title 


class Student(models.Model):
    name = models.CharField(max_length=25, unique=True)
    email = models.EmailField()
    course = models.ForeignKey(Course, related_name="student", on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f"Aty:> {self.name}: Pochtasy:> {self.email}"



