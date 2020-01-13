from django.contrib import admin
from .models import Clinic, Profile, Comments, Ocenka


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Profile)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'type')
    list_filter = ('profession', )

admin.site.register(Comments)
admin.site.register(Ocenka)