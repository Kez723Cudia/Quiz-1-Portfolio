from django.db import models

class Testimony(models.Model):
    full_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.full_name} - {self.content[:30]}"

# Create your models here.
