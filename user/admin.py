from django.contrib import admin


from .models import UserProfile,AppliedJob

# Optionally, you can create a custom ModelAdmin class to customize how your model is displayed in the admin interface
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'age', 'address', 'profile_image','password')  # Fields to display in the list view
    search_fields = ('full_name', 'email')  # Fields to search by in the admin
    list_filter = ('age',)  # Filter by age or other fields
    ordering = ('full_name',)  # Default ordering of the list view

class AppliedJobAdmin(admin.ModelAdmin):
    list_display = ('applied_on', 'user', 'job')  # Fields to display in the list view

# Register the model with the admin interface
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(AppliedJob, AppliedJobAdmin)

