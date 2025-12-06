from django.contrib import admin
from .models import Project, Skill, ContactMessage ,TimelineItem 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'created_at')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'icon',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display =('name','email','subject','created_at',)

@admin.register(TimelineItem)
class TimeLineItemAdmin(admin.ModelAdmin):
    list_display = ('category','title', 'start_year', 'end_year')