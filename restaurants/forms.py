from django import forms 
from .models import *
from .validators import *

# class RestaurantCreateForm(forms.Form):
# 	name 		= forms.CharField()
# 	location 	= forms.CharField(required=False)
# 	category 	= forms.CharField(required=False)


class RestaurantModelForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = [
			'name',
			'location',
			'category'

		]
