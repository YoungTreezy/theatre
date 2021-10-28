from django.contrib import admin
from .models import (University, Actors, Info_about_university, GlobalInformation)


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',) # display
    search_fields = ['name']
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ('master', 'slug', 'university')
    # list_filter = ('master', 'university') #right filter
    search_fields = ('master', 'university')
    raw_id_fields = ('university',) # easy search in ForeignKey
    prepopulated_fields = {'slug': ('master',)}


@admin.register(Info_about_university)
class Info_about_universityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'university')
    raw_id_fields = ('university',)


@admin.register(GlobalInformation)
class GlobalInformationAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    search_fields = ('title',)
    raw_id_fields = ('university',)
    prepopulated_fields = {'slug': ('title',)}
