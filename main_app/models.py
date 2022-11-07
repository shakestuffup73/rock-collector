from django.db import models

# Create your models here.
class Rock(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  hardness = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
