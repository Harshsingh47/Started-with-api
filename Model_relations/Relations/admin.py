from django.contrib import admin
from .models import Posts,Creators,Aricle,Publication,Article,UserDetails,Working
# Register your models here.


admin.site.register(Aricle)
# admin.site.register(Customer)
# admin.site.register(Products)
admin.site.register(Posts)
admin.site.register(Creators)
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(UserDetails)
admin.site.register(Working)
