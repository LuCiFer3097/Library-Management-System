from django.contrib import admin

# Register your models here.

from .models import Category,Publisher,Author,Book,review#,token

admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(review)
