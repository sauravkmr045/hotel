from django.db import models

# Create your models here.

class HotelDetail(models.Model):

	hotel_name= models.CharField(max_length=250,blank= True, null=True)
	room_availability = models.CharField(max_length=250,blank= True, null=True)
	price = models.IntegerField(blank= True, null=True)
	hotel_address = models.CharField(max_length=250, blank= True, null=True)
	hotel_mobile = models.CharField(max_length=10,blank= True, null=True)
	updated_at =   models.DateTimeField(auto_now_add=True)
   
	image = models.ImageField(upload_to='images', null=True, blank=True)
    
	hotel_detail = models.TextField(blank= True, null=True)

	def __str__(self):
		return self.hotel_name
    	

class ContactUs(models.Model):

	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=80)
	mobile = models.CharField(max_length=10)
	message = models.TextField()

	def __str__(self):
		return self.name
