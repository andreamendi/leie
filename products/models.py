from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 60, null = False)
	description = models.TextField(max_length = 400, null = False)
	rent_days = models.IntegerField(default = 1,null = False)
	quality = models.IntegerField(default = 1)
	brand = models.CharField(max_length = 50)
	taken = models.BooleanField(null = False)
	price = models.FloatField(default=0.01)
	comments = models.TextField(max_length = 180, null = False)
	# ranking_product = models.ManyToManyField(User, through='RankingProduct') Ver donde pongo esto, ya que no está el user
	create_at = models.DateTimeField(auto_now_add=True) #Here we've the date when the user will create the product
	modified_at = models.DateTimeField(auto_now=True) #Here we've the date when the user modify the product

class Category(models.Model):
	name = models.CharField(max_length = 100, null = False)
	create_at = models.DateTimeField(auto_now_add=True) #Here we've the date when the user will create the product
	modified_at = models.DateTimeField(auto_now=True) #Here we've the date when the user modify the product

class Card(models.Model):
	card_number = models.CharField(max_length = 50, null = False)
	secure_number = models.CharField(max_length = 4, null = False)
	valid_thru = models.CharField(max_length = 4, null = False)
	create_at = models.DateTimeField(auto_now_add=True) #Here we've the date when the user will create the product
	modified_at = models.DateTimeField(auto_now=True) #Here we've the date when the user modify the product
	# user = models.ForeignKey(Reporter)

class RankingProduct(models.Model):
  # user = models.ForeignKey(User)
  # products = models.ForeignKey(Products)
	score = models.IntegerField(default = 0)
	begin_day =  models.TimeField(auto_now = False,null = False)
	end_day = models.TimeField(auto_now = False,null = False)
	create_at = models.DateTimeField(auto_now_add=True) #Here we've the date when the user will create the product
	modified_at = models.DateTimeField(auto_now=True) #Here we've the date when the user modify the product