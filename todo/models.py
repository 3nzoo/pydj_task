from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.title

