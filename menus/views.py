from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView 
from .models import *  
from .forms import * 


# Create your views here.
class ItemListView(ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView):
	form_class = ItemForm
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemUpdateView(UpdateView):
	form_class = ItemForm
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

