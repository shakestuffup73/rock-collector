from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Rock, Frog
from .forms import FeedingForm

# Create your views here.

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def rocks_index(request):
  rocks = Rock.objects.filter(user=request.user)
  return render(request, 'rocks/index.html', {'rocks' : rocks })

@login_required
def rocks_detail(request, rock_id):
  rock = Rock.objects.get(id=rock_id)
  frogs_rock_doesnt_have = Frog.objects.exclude(id__in = rock.frogs.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'rocks/detail.html', {
    'rock': rock, 'feeding_form': feeding_form, 'frogs': frogs_rock_doesnt_have
  })

@login_required
def add_feeding(request, rock_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.rock_id = rock_id
    new_feeding.save()
  return redirect('rocks_detail', rock_id=rock_id)

class RockCreate(LoginRequiredMixin, CreateView):
  model = Rock
  fields = ['name', 'type', 'color']
  success_url = '/rocks/'

  def form_valid(self, form):
    form.instance.user = self.request.user

    return super().form_valid(form)

class RockUpdate(LoginRequiredMixin, UpdateView):
  model = Rock
  fields = ['color', 'hardness']

class RockDelete(LoginRequiredMixin, DeleteView):
  model = Rock
  success_url = '/rocks/'

class FrogCreate(LoginRequiredMixin, CreateView):
  model = Frog
  fields = '__all__'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('frogs_detail', kwargs={'pk': self.id})


class FrogList(LoginRequiredMixin, ListView):
  model = Frog

class FrogDetail(LoginRequiredMixin, DetailView):
  model = Frog

class FrogUpdate(LoginRequiredMixin, UpdateView):
  model = Frog
  fields = ['name', 'size']

class FrogDelete(LoginRequiredMixin, DeleteView):
  model = Frog
  success_url = '/frogs/'

@login_required
def assoc_frog(request, rock_id, frog_id):
  Rock.objects.get(id=rock_id).frogs.add(frog_id)
  return redirect('rocks_detail', rock_id=rock_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('rocks_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)