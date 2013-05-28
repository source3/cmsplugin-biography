from django.contrib import admin

from .models import PersonBiography


class PersonBiographyAdmin(admin.ModelAdmin):
    search_fields = ('^last_name', '^first_name', )

admin.site.register(PersonBiography, PersonBiographyAdmin)
