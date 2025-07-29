from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    url = models.URLField(blank=True)
    github = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
    
class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.role} at {self.company}"
    
class Certificate(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date_issued = models.DateField()
    description = models.TextField(blank=True)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='certificate_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} from {self.issuer}"
    
    class Meta:
        ordering = ['-date_issued']