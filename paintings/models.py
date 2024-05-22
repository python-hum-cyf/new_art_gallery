# Create your models here.

from django.db import models

# Create your models here.

class Painting(models.Model):

    title = models.CharField(max_length=100, default='Unknown')
    author = models.ForeignKey('painters.Painter', null=True, on_delete=models.SET_NULL)
    on_loan = models.BooleanField(default=False, verbose_name='LOANED')


    def __str__(self):
        return self.title
