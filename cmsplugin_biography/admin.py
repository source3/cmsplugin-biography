from django.contrib import admin

from .models import PersonBiography


class PersonBiographyAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'title', 'employer', 'active', )
    list_filter = ('active', )
    search_fields = ('^last_name', '^first_name', )

admin.site.register(PersonBiography, PersonBiographyAdmin)
