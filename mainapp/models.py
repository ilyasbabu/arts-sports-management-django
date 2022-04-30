from django.db import models

# Create your models here.
class AdmissionNumbers(models.Model):
    admission_number = models.CharField(max_length=4)
    def __str__(self):
        return self.admission_number