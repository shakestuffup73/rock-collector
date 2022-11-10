from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Rock, Frog
from .forms import FeedingForm

# Create your views here.

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def rocks_index(request):
  rocks = Rock.objects.all()
  return render(request, 'rocks/index.html',
  {'rocks' : rocks })

def rocks_detail(request, rock_id):
  rock = Rock.objects.get(id=rock_id)
  frogs_rock_doesnt_have = Frog.objects.exclude(id__in = rock.frogs.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'rocks/detail.html', {
    'rock': rock, 'feeding_form': feeding_form, 'frogs': frogs_rock_doesnt_have
  })

def add_feeding(request, rock_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.rock_id = rock_id
    new_feeding.save()
  return redirect('rocks_detail', rock_id=rock_id)

class RockCreate(CreateView):
  model = Rock
  fields = '__all__'
  success_url = '/rocks/'

class RockUpdate(UpdateView):
  model = Rock
  fields = ['color', 'hardness']

class RockDelete(DeleteView):
  model = Rock
  success_url = '/rocks/'

class FrogCreate(CreateView):
  model = Frog
  fields = '__all__'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('frogs_detail', kwargs={'pk': self.id})


class FrogList(ListView):
  model = Frog

class FrogDetail(DetailView):
  model = Frog

class FrogUpdate(UpdateView):
  model = Frog
  fields = ['name', 'size']

class FrogDelete(DeleteView):
  model = Frog
  success_url = '/frogs/'

def assoc_frog(request, rock_id, frog_id):
  Rock.objects.get(id=rock_id).frogs.add(frog_id)
  return redirect('rocks_detail', rock_id=rock_id)