from django.shortcuts import render
from .models import Rock

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Rock: 
  def __init__(self, name, type, color, hardness):
    self.name = name
    self.type = type
    self.color = color
    self.hardness = hardness


rocks = [
  Rock('Granite', 'Igneous', 'grey', 'hardAF',),
  Rock('Basalt', 'Igneous', 'dark-grey', 'mid'),
  Rock('Obsidian', 'Igneous', 'black', 'mid')
]

def rocks_index(request):
  return render(request, 'rocks/index.html',
  {'rocks' : rocks })