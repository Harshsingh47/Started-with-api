from django.contrib import admin
from .models import Posts,Creators,Aricle
# Register your models here.


admin.site.register(Aricle)
# admin.site.register(Customer)
# admin.site.register(Products)
admin.site.register(Posts)
admin.site.register(Creators)
