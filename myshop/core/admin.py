from django.contrib import admin

from django.contrib import admin
from .models import Seller, Package, Buyer, Purchase

class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('user__username',)

admin.site.register(Seller, SellerAdmin)
admin.site.register(Package)
admin.site.register(Buyer)
admin.site.register(Purchase)

