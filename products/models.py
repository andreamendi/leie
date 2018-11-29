from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 100, null = False)
	create_at = models.DateTimeField(auto_now_add=True) # Here we've the date when the user will create the product
	modified_at = models.DateTimeField(auto_now=True) # Here we've the date when the user modify the product

	def __str__(self):
		return 'Name: {}'.format(self.name)


class Product(models.Model):
	name = models.CharField(max_length = 60, null = False)
	description = models.TextField(max_length = 400, null = False)
	rent_days = models.IntegerField(default = 1,null = False)
	quality = models.IntegerField(default = 1)
	brand = models.CharField(max_length = 50)
	taken = models.BooleanField(null = False)
	price = models.FloatField(default=0.01)
	comments = models.TextField(max_length = 180, null = False)
	user = models.ForeignKey(User, on_delete=models.CASCADE) #La FK se pone en la que no es la "dueña"
	rents = models.ManyToManyField(User, through='Rent', related_name='rents') # Tu tienes una relación con User ManyToMany
	categories = models.ManyToManyField(Category)
	create_at = models.DateTimeField(auto_now_add=True) # Here we've the date when the user will create the product
	modified_at = models.DateTimeField(auto_now=True) # Here we've the date when the user modify the product

	def __str__(self):
		return 'Name: {}, user: {}'.format(self.name,self.user)





class Card(models.Model):
	card_number = models.CharField(max_length = 50, null = False)
	secure_number = models.CharField(max_length = 4, null = False)
	valid_thru = models.CharField(max_length = 4, null = False)
	full_name = models.CharField(max_length = 100, null = False)
	create_at = models.DateTimeField(auto_now_add=True) # Here we've the date when the user will create the product
	modified_at = models.DateTimeField(auto_now=True) # Here we've the date when the user modify the product
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return 'Fullname: {}, user: {}'.format(self.full_name,self.user)


class Rent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	score = models.IntegerField(default = 0)
	begin_day =  models.TimeField(auto_now = False,null = False)
	end_day = models.TimeField(auto_now = False,null = False)
	create_at = models.DateTimeField(auto_now_add=True) #Here we've the date when the user will create the product
	modified_at = models.DateTimeField(auto_now=True) #Here we've the date when the user modify the product
	
	def __str__(self):
		return 'User: {}, Product: {}'.format(self.user,self.product)