from django.db import models


class TechStack(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name



class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    tech_stacks = models.ManyToManyField(
        TechStack,
        related_name="projects",
    )

    link = models.URLField()

    def __str__(self):
        return self.project_name

# Create your models here.
