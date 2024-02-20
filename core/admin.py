from django.contrib import admin
from . import models


@admin.register(models.Department)
class Department(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(models.Author)
class Author(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(models.Book)
class Book(admin.ModelAdmin):
    search_fields = ('name', )
    autocomplete_fields = ('author', 'department')
