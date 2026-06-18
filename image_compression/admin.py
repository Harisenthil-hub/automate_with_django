from django.contrib import admin
from .models import CompressImage
from django.utils.html import format_html

# Register your models here.

class CompressImageAdmin(admin.ModelAdmin):
    
    def thumbnail(self, obj):
        return format_html("<img src='{}' width='40' height='40'>", obj.compressed_img.url)
    
    def org_img_size(self, obj):
        size_in_mb = round(obj.original_img.size / (1024*1024), 2)
        if size_in_mb > 1:
            return format_html('{} MB', size_in_mb)
        else:
            size_in_kb = round(obj.original_img.size / 1024, 2)
            return format_html('{} KB',size_in_kb )
            
    
    def comp_img_size(self, obj):
        size_in_mb = round(obj.compressed_img.size / (1024*1024), 2)
        if size_in_mb > 1:
            return format_html('{} MB',size_in_mb )
        else:
            size_in_kb = round(obj.compressed_img.size / 1024, 2)
            return format_html('{} KB',size_in_kb )
            
    
    list_display = ['user', 'thumbnail', 'org_img_size', 'comp_img_size', 'compressed_at']



admin.site.register(CompressImage, CompressImageAdmin)
