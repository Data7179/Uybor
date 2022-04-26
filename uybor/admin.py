from turtle import mode
from django.contrib import admin
from .models import Uylar

# Register your models here.

class UylarAdmin(admin.ModelAdmin):
    list_display = ("id", "viloyat", "tuman", "xonalar_soni")
    search_fields = ("viloyat", "tuman", "uy_turi")
    list_filter = ("viloyat", )
admin.site.register(Uylar, UylarAdmin)
