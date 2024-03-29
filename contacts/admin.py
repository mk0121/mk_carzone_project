from django.contrib import admin
from .models import Contacts

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','car_title','email','city','create_date')
    list_display_link = ('id','first_name','last_name')
    search_fields = ('first_name','last_name','email','car_title')
    list_per_page = 25

admin.site.register(Contacts,ContactAdmin)