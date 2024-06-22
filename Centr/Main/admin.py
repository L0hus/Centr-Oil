from django.contrib import admin
from .models import Product
from .models import Feedback

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'id', 'typeForName', 'name', 'gost', 'base', 'pack', 'area', 'feature', 'characteristic', 'image2')
    search_fields = ('type', 'id')
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'ip_address', 'submitted_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('ip_address', 'submitted_at')
