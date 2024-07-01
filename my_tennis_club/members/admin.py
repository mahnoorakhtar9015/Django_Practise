from django.contrib import admin

# Register your models here.
from .models import members


class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date")

admin.site.register(members,MemberAdmin)