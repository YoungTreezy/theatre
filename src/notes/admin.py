from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created']
    search_fields = ['title', 'author']
    fieldsets = (
        ('Add note', {
            'fields': ('title', 'slug', 'description', 'finish')
        }),
    )
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
