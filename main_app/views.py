from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

class Rock: 
  def __init__(self, name, type, color, hardness, luster, crystalForms):
    self.name = name
    self.type = type
    self.color = color
    self.hardness = hardness
    self.luster = luster
    self.crystalForms = crystalForms


rocks = [
  Rock('Granite', 'Igneous', 'grey', 'hardAF', 'vitreous', 'mica & quartz'),
  Rock('Basalt', 'Igneous', 'dark-grey', 'mid', 'glassy', 'olivine, pyroxene & plagiocase'),
  Rock('Obsidian', 'Igneous', 'black', 'mid', 'glassy lustre', 'silica')
]

def rocks_index(request):
  return render(request, 'rocks/index.html',
  {'rocks' : rocks })