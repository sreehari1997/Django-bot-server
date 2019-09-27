from django.db import models

# Create your models here.

class Buttoncount(models.Model):
    user = models.CharField(max_length=20) 
    fat = models.PositiveIntegerField(default=0)
    dumb = models.PositiveIntegerField(default=0)
    stupid = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user