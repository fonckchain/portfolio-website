from django.contrib import admin
from .models import SocialLink, ContactMessage, Technology, Skill, Project

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'display_name', 'url', 'order', 'is_active')
    list_filter = ('platform', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('display_name', 'url')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read', 'replied')
    list_filter = ('is_read', 'replied', 'created_at')
    list_editable = ('is_read', 'replied')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency_level', 'is_interested')
    list_filter = ('category', 'is_interested')
    search_fields = ('name', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('title', 'description')
    filter_horizontal = ('technologies', 'skills')