from django.contrib import admin
from .models import Post, Contact


@admin.register(Post)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'image', 'body', 'year', 'price', 'engine', 'wheel')

@admin.register(Contact)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone')