from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
  ('MR', 'Mushies'),
  ('MO', 'Moss'),
  ('L', 'Lichen'),
)

SPECIES = (
  ('B', 'BullFrog'),
  ('P', 'PennyFrog'),
  ('T', 'TreeFrog'),
  ('K', 'Kermit'),
)

SIZE = (
  ('V', 'very smol'),
  ('S', 'smol'),
  ('M', 'midsize'),
  ('L', 'large'),
  ('T', 'thicc'),
  ('B', 'bigboi')
)

# Create your models here.
class Frog(models.Model):
  name = models.CharField(
    max_length=50,
    default='Chonk'
  )
  size = models.CharField(
    max_length=10,
    default=SIZE[0][0]
  )
  species = models.CharField(
    max_length=50,
    default=SPECIES[0][1]
  )
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('frogs_detail', kwargs={'pk': self.id})

class Rock(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  frogs = models.ManyToManyField(Frog)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

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

