from django.contrib import admin
from .models import Painter

# Register your models here.

class PainterAdmin(admin.ModelAdmin):
    list_display = ['name', 'period']
    search_fields = ['name']
    readonly_fields = ['age']

    def age(self, instance):
        if instance.year_of_birth == 'Unknown' or instance.year_of_death == 'Unknown':
            return 'Unknown'
        age = instance.year_of_death - instance.year_of_birth
        return age if age > 0 else 'Unknown'

admin.site.register(Painter, PainterAdmin)
