from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from restaurants.utils import unique_slug_generator
from django.core.urlresolvers import reverse
from .validators import *

User = settings.AUTH_USER_MODEL

# Create your models here.
class Restaurant(models.Model):
	owner 		= models.ForeignKey(User)
	name 		= models.CharField(max_length=120)
	location 	= models.CharField(max_length=120, null=True, blank=True)
	category 	= models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
	timestamp	= models.DateTimeField(auto_now_add=True)
	updated  	= models.DateTimeField(auto_now=True)
	slug  		= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants-detail', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.name

def rest_pre_save_reciever(sender, instance, *args, **kwargs):
	instance.category = instance.category.capitalize()
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

# def rest_post_save_reciever(sender, instance,created, *args, **kwargs):
# 	print('saved')
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)
# 		instance.save()

pre_save.connect(rest_pre_save_reciever, sender=Restaurant)
# post_save.connect(rest_post_save_reciever, sender=Restaurant)
