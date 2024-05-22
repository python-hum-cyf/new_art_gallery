from django.db import models

# Create your models here.

class Painter(models.Model):
    PERIOD_CHOICES = (
        ('M', 'Medieval'),
        ('R', 'Renaissance'),
        ('B', 'Baroque'),
        ('U', 'Unknown'),
    )
    name = models.CharField(max_length=100, default='Anonymous')
    period = models.CharField(max_length=1, choices=PERIOD_CHOICES, default='U')
    year_of_birth = models.IntegerField(default=9999)
    year_of_death = models.IntegerField(default=0)

    def __str__(self):
        return self.name

