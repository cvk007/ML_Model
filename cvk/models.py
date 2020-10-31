from django.db import models


# Create your models here.
class feedback(models.Model):

    name = models.TextField()
    email = models.TextField()
    subject = models.TextField()
    patient = models.CharField(max_length=30)

    def __str__(self):
        return self.name
