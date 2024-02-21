from django.contrib import admin
from . import models


class HandedBookInline(admin.TabularInline):
    model = models.HandedBook
    extra = 0


@admin.register(models.Department)
class Department(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(models.Author)
class Author(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(models.Book)
class Book(admin.ModelAdmin):
    inlines = (HandedBookInline, )
    search_fields = ('name', )
    autocomplete_fields = ('author', 'department')


@admin.register(models.Client)
class Client(admin.ModelAdmin):
    inlines = (HandedBookInline, )
    search_fields = ('name', )
