from django.contrib import admin
from .models import Book,Bookstore,Author,Order

class BookstoreInline(admin.TabularInline):
    model = Bookstore

class BookAdmin(admin.ModelAdmin):
    inlines = [BookstoreInline]


admin.site.register(Bookstore)
admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Order)