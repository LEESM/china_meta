from django.contrib import admin
from item.models import Item, ItemLink
from django_summernote.admin import SummernoteModelAdmin

class ItemAdmin(SummernoteModelAdmin):
	list_display = ['brand', 'title','image','pub_date','detail','main1','main2',]

class ItemLinkAdmin(admin.ModelAdmin):
	list_display = ['item','source_name','source_url','price','delivery','additional_benefit',]

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemLink, ItemLinkAdmin)
