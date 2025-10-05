from django.db import models

class Technology(models.Model):
    """Technologies I use or am interested in learning"""
    CATEGORY_CHOICES = [
        ('language', 'Programming Language'),
        ('framework', 'Framework'),
        ('database', 'Database'),
        ('tool', 'Tool'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    icon_url = models.URLField(blank=True, help_text="URL to technology icon/logo")
    proficiency_level = models.IntegerField(
        default=50,
        help_text="Proficiency level from 0-100"
    )
    is_interested = models.BooleanField(
        default=False,
        help_text="Mark if interested in learning (vs currently using)"
    )

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['-proficiency_level', 'name']

    def __str__(self):
        return self.name

class Skill(models.Model):
    """Specific skills and competencies"""
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField()
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g., Backend, Frontend, DevOps, etc."
    )

    def __str__(self):
        return self.name

class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name='projects')
    skills = models.ManyToManyField(Skill, blank=True, related_name='projects')
    link = models.URLField(blank=True, help_text="Live project URL")
    github_url = models.URLField(blank=True, help_text="GitHub repository URL")
    image_url = models.URLField(blank=True, help_text="Project screenshot/image URL")
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.title