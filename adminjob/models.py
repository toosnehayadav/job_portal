from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=255)  # Job name (up to 255 characters)
    experience = models.CharField(max_length=255)  # Experience requirements (up to 255 characters)
    detail = models.TextField()  # Detailed description of the job
    image = models.ImageField(upload_to='job_images/', null=True, blank=True)  # Optional image field
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salary (e.g., 99999999.99)
    address  = models.CharField(max_length=255,default="Mumbai",null=True)

    def __str__(self):
        return self.job_name
