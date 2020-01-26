from django.contrib import admin
from .models import Book
"""

    NOTE: to operate the django admin page,

    ./manage.py createsuperuser



    This is admin class for registering book model to
    bookadmin, in Django Admin page.

    By default, not everything is managable on django admin page
    to model reisgter, one has to create an extended class for admin.ModelAdmin

    After this registering, they aare managable on admin page

"""
class BookAdmin(admin.ModelAdmin):
    """docstring for BookAdmin.admin.ModelAdmin"""
    list_display = ['title','author', 'price', 'stock']

admin.site.register(Book, BookAdmin)
