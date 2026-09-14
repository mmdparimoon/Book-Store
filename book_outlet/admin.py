from django.contrib import admin
from .models import Book,Author,Address,Country
# Register your models here.



class BookAdmin(admin.ModelAdmin):
    
    prepopulated_fields={'slug':('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'author', 'rating', 'is_bestselling',)
    
class AuthorAdmin(admin.ModelAdmin):

    list_display=('last_name','first_name','address',)
   
    
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)