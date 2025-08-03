from django.contrib import admin
from .models import Project, WorkExperience, Certificate

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at')
    search_fields = ('title', 'description', 'technology')
    list_filter = ('technology', 'created_at')

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'start_date', 'end_date', 'current')
    search_fields = ('company', 'role', 'description')
    list_filter = ('current', 'start_date', 'end_date')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date_issued')
    search_fields = ('title', 'issuer', 'description', 'credential_id')
    list_filter = ('issuer', 'date_issued')
    date_hierarchy = 'date_issued'