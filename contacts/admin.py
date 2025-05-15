from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('listing', 'id', 'name', 'email', 'phone', 'contact_date')
    list_display_links = ( 'listing', 'name')
    search_fields = ('listing', 'name', 'email')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)