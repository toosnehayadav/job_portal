from django.contrib import admin
from .models import Job
# Register your models here.
# Optionally, you can create a custom ModelAdmin class to customize how your model is displayed in the admin interface
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'experience', 'detail', 'image', 'salary')  # Fields to display in the list view
    search_fields = ('job_name', 'email')  # Fields to search by in the admin


# Register the model with the admin interface
admin.site.register(Job, JobAdmin)