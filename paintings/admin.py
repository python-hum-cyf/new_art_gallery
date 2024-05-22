from django.contrib import admin
from .models import Painting


@admin.action(description='Toggle loan status')
def toggle_loaned(_modeladmin, _request, queryset):
    for obj in queryset:
        obj.on_loan = not obj.on_loan
        obj.save()


class PaintingAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'on_loan', ]
    raw_id_fields = ['author']
    actions = [toggle_loaned]


admin.site.register(Painting, PaintingAdmin)
