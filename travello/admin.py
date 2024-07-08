# from django.contrib import admin
# from .models import Destination
# # Register your models here.

# admin.site.register(Destination)

# from django.contrib import admin
# from .models import Destination

# class DestinationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'offer', 'slug')  # Fields to display in the list view
#     search_fields = ('name', 'desc')  # Fields to search
#     list_filter = ('offer',)  # Filters to display
#     prepopulated_fields = {'slug': ('name',)}  # Prepopulate slug field based on name
#     fields = ('name', 'slug', 'desc', 'price', 'offer', 'image') # image filed hee is very important for it to add or edit an image after Destination object creation
      

# admin.site.register(Destination, DestinationAdmin)


from django.contrib import admin
from django.utils.html import format_html
from .models import Destination

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'offer', 'slug', 'image_preview')  # Add image_preview to list_display
    search_fields = ('name', 'desc')
    list_filter = ('offer',)
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'desc', 'price', 'offer', 'image', 'image_preview')  # Include image and image_preview in form

    readonly_fields = ('image_preview',)  # Make image_preview read-only

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return "No Image"

    image_preview.short_description = 'Image Preview'

admin.site.register(Destination, DestinationAdmin)
