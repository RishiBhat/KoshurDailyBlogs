from django.contrib import admin
from .models import Blog, Author, Book, Articles

# Register your models here.


admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Book)
admin.site.register(Articles)
