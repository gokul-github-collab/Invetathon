from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10)
    image = models.ImageField(upload_to="student_images/")
    program = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    # Add other student-related fields

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    faculty_id = models.CharField(max_length=10)
    image = models.ImageField(upload_to="faculty_images/")
    department = models.CharField(max_length=100)
    # Add other faculty-related fields

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    # Add other project-related fields

    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='module_images/')
    # Add other module-related fields

    def __str__(self):
        return self.title

class ModuleRating(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    # Add other fields related to module rating

    def __str__(self):
        return f"{self.module} - {self.faculty}"

class Comment(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author} on {self.module.title}"