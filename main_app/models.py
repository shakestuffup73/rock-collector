from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('MR', 'Mushies'),
  ('MO', 'Moss'),
  ('L', 'Lichen'),
  ('P', 'Prickly Pear')
)
# Create your models here.
class Rock(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  hardness = models.CharField(max_length=100)

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("rocks_detail", kwargs={"rock_id": self.id})
  
class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=2,
    choices=MEALS,
    default=MEALS[1][0]
  )

  rock = models.ForeignKey(Rock, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
    
  class Meta:
    ordering = ['-date']

class Tumbled(models.Model):
  hours = models.IntegerField()
  tumbler_brand = models.CharField(max_length=50)
  grit_type = models.CharField(max_length=50)
  grit_brand = models.CharField(max_length=50)

