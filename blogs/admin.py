from django.contrib import admin
from .models import User, Blog

class UserModel(admin.ModelAdmin):
	list_display = ('username', 'fname', 'lname', 'email', 'password')

class BlogModel(admin.ModelAdmin):
	list_display = ('title', 'user', 'pub_date')

admin.site.register(User, UserModel)
admin.site.register(Blog, BlogModel)
