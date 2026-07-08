from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.project_name

# Create your models here.
