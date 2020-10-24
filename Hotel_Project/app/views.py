from django.shortcuts import render
from .models import HotelDetail,ContactUs
from django.contrib.auth import logout
# Create your views here.

def home(request):

	hotel = HotelDetail.objects.all().order_by('-updated_at')

	return render(request,'home.html',{'hotel': hotel})


def services(request):

	return render(request,'services.html')

def contact(request):
	if request.method =="POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		message = request.POST.get('message')

		data = ContactUs(name= name, email=email, mobile=mobile, message=message)
		data.save()
		msg = "Your Query has been submitted successfuly we will get back to you soon"
		return render(request,'contact.html',{'msg':msg})



	return render(request,'contact.html')


def booking(request):

	return render(request, 'booking.html')


def glogin(request):

	return render(request, 'glogin.html')

def glogout(request):
    logout(request)
    return render(request,'glogin.html')
