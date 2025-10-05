from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'is_featured', 'completion_date')
    list_filter = ('category', 'is_featured', 'completion_date')
    search_fields = ('title', 'client', 'description', 'technologies_used')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'completion_date'
    list_editable = ('is_featured',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'client', 'description', 'full_case_study')
        }),
        ('Media & Links', {
            'fields': ('image', 'website_url', 'github_url')
        }),
        ('Categorization', {
            'fields': ('category', 'technologies_used', 'is_featured')
        }),
        ('Timeline', {
            'fields': ('completion_date',)
        }),
    )