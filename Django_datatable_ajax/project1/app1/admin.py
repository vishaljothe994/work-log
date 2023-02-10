from django.contrib import admin
from .models import Member


# Register your models here.
@admin.register(Member)
class MemberModelAdmin(admin.ModelAdmin):
 list_display=['id', 'firstname', 'lastname', 'address']

# admin.site.register(Member)