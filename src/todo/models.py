from django.db import models

from django.db import models




class DoList(models.Model):
    line = models.CharField(max_length=255)
    complite = models.BooleanField(default=False)

    # Create your models here.
    def __str__(self):
        return self.line
