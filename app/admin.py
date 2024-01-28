from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
# from simple_history.forms import SimpleHistoryForm

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contract_number', 'get_items']

    def get_items(self, obj):
        return ', '.join([item.name for item in obj.items_owned.all()])

    get_items.short_description = 'Items Owned'
    
@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display=['name','user','category','handover_time','receive_time']