from django.db import models

class Inquiry(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"Inquiry from {self.first_name} {self.last_name}"

# Create your models here.
