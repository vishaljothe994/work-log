from django.contrib import admin
from .models import Post
# # Register your models here.

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#  list_display=('id', 'stuid', 'stuname', 'stuemail', 'stupass')

admin.site.register(Post)

