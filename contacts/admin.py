from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'service_of_interest', 'submitted_at', 'is_addressed')
    list_filter = ('is_addressed', 'submitted_at', 'service_of_interest')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('name', 'email', 'company', 'service_of_interest', 'message', 'submitted_at')
    list_editable = ('is_addressed',)
    date_hierarchy = 'submitted_at'
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'company', 'service_of_interest')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Metadata', {
            'fields': ('submitted_at', 'is_addressed')
        }),
    )