from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('rocks/', views.rocks_index, name='rocks_index'),
  path('rocks/<int:rock_id>/', views.rocks_detail, name='rocks_detail'),
  path('rocks/create/', views.RockCreate.as_view(), name='rocks_create'),
  path('rocks/<int:pk>/update/', views.RockUpdate.as_view(), name='rocks_update'),
  path('rocks/<int:pk>/delete/', views.RockDelete.as_view(), name='rocks_delete'),
  path('rocks/<int:rock_id>/add_feeding', views.add_feeding, name='add_feeding'),
  path('rocks/<int:rock_id>/assoc_frog/<int:frog_id>/', views.assoc_frog, name='assoc_frog'),
  path('frogs/create/', views.FrogCreate.as_view(), name='frogs_create'),
  path('frogs/<int:pk>/', views.FrogDetail.as_view(), name='frogs_detail'),
  path('frogs/', views.FrogList.as_view(), name='frogs_index'),
  path('frogs/<int:pk>/update/', views.FrogUpdate.as_view(), name='frogs_update'),
  path('frogs/<int:pk>/delete/', views.FrogDelete.as_view(), name='frogs_delete'),
  path('accounts/signup/', views.signup, name='signup')
]