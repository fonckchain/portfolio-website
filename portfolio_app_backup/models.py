from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField()  # 1-100 for percentage
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Skill)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title