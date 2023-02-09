from django.db import models
from django.urls import reverse
# Create your models here.

class Phone(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    screen = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={
        'phone_id': self.id
        })