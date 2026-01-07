from django.contrib import admin
from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description')
    search_fields = ('name',)
    list_filter = ('age',)
admin.site.register(Pet, PetAdmin)
