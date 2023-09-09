from django.contrib import admin
from .models import Employee, EventType, Event, EmailTemplate
# Register your models here.


# We use here the @admin.register decorator to register each model for administration in the Django admin interface.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birth_date', 'joining_date')
    search_fields = ('name', 'email')
    list_filter = ('birth_date', 'joining_date')

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('employee', 'event_type', 'event_date')
    list_filter = ('event_type', 'event_date')
    search_fields = ('employee__name', 'employee__email')

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'subject', 'template_name')    