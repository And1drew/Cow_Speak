from django.db import models

# Create your models here.
class Cow_talk(models.Model):
    text = models.CharField(max_length=39)
    def __str__(self):
        return self.text