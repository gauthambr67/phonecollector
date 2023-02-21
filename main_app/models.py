from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User 
# Create your models here.

CHARGES = (('M', 'Morning'),
           ('A', 'Afternoon'),
           ('N', 'Night'),
           )

class Accessory(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("accessories_detail", kwargs={'pk': self.id})

class Phone(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    screen = models.DecimalField(max_digits=4, decimal_places=2)
    accessories = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.model} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={
        'phone_id': self.id
        })

    def charged_for_today(self):
        return self.charging_set.filter(date=date.today()).count()


class Charging(models.Model):   
    date=models.DateField('Charging Date')
    charge = models.CharField(
        max_length=1,
        choices=CHARGES,
        default=CHARGES[0][0]
    )

    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_charge_display()} on {self.date}"
    
    class Meta:
        ordering = ["-date"]

class Photo(models.Model):
    url = models.CharField(max_length=255)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for phone_id: {self.phone_id} @{self.url}"