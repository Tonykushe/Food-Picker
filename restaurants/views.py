from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.

def restaurant_createview(request):
	form = RestaurantModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/restaurants/')
	template_name = 'restaurants/form.html'
	context = {'form': form}
	return render(request, template_name, context)



# def restaurant_list(request):
# 	template_name = 'restaurants/restaurants_list.html'
# 	queryset = Restaurant.objects.all()
# 	context = {
# 		'object_list': queryset
# 	}
# 	return render(request, template_name, context)

class RestaurantListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get('slug')
		if slug:
			queryset = Restaurant.objects.filter(
					Q(category__iexact=slug) |
					Q(category__icontains=slug)
				)
		else:
			queryset = Restaurant.objects.all()

		return queryset

class RestaurantDetailView(DetailView):
	queryset = Restaurant.objects.all()


class RestaurantCreateView(CreateView):
	form_class = RestaurantModelForm
	template_name = 'restaurants/form.html'
	success_url = '/restaurants'


	