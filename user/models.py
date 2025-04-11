
from django.db import models
from adminjob.models import Job
class UserProfile(models.Model):
    full_name = models.CharField(max_length=255, default="")
    email = models.EmailField(unique=True,default="")
    phone_number = models.CharField(max_length=15, default="")
    age = models.PositiveIntegerField()
    address = models.TextField(default="")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    password = models.CharField(max_length=255,default="")

    def __str__(self):
        return self.full_name


class AppliedJob(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # ForeignKey to UserProfile
    job = models.ForeignKey(Job, on_delete=models.CASCADE)  # Correct reference to the Job model in the 'jobs' app
    applied_on = models.DateTimeField(auto_now_add=True)  # To track when the user applied

    class Meta:
        unique_together = ('user', 'job')  # Ensures that a user can only apply for the same job once

    # def __str__(self):
    #     return f"{self.user.full_name} applied for {self.job.job_name}"