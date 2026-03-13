from django.contrib import admin
from .models import Product, Review, ContactMessage

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'get_discounted_price', 'created_at')
    list_filter = ('discount', 'created_at')
    search_fields = ('name', 'description')
    list_per_page = 10
    readonly_fields = ('created_at',)
    
    def get_discounted_price(self, obj):
        return f"${obj.get_discounted_price():.2f}"
    get_discounted_price.short_description = 'Final Price'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'message_preview', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'message')
    list_per_page = 10
    readonly_fields = ('created_at',)
    
    def message_preview(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
    list_per_page = 10
    readonly_fields = ('created_at',)