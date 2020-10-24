from django.contrib import admin
from .models import HotelDetail,ContactUs
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class HotelDetailAdmin(admin.ModelAdmin):
	list_display = ['hotel_name','room_availability','price','hotel_address','hotel_mobile','updated_at','hotel_detail']

admin.site.register(HotelDetail,HotelDetailAdmin)


class ContactUsAdmin(admin.ModelAdmin):
	list_display = ['id','name','email','mobile','message']

admin.site.register(ContactUs,ContactUsAdmin)