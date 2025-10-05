from django.db import models

class Project(models.Model):
    PROJECT_CATEGORY = [
        ('WEB', 'Web Development'),
        ('SOFT', 'Software Solution'),
        ('CONS', 'Consulting'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True) # For SEO-friendly URLs
    client = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    full_case_study = models.TextField(blank=True) # Detailed case study
    category = models.CharField(max_length=5, choices=PROJECT_CATEGORY)
    image = models.ImageField(upload_to='portfolio/')
    website_url = models.URLField(blank=True, verbose_name="Project URL")
    github_url = models.URLField(blank=True)
    technologies_used = models.CharField(max_length=200, help_text="Comma-separated list")
    is_featured = models.BooleanField(default=False)
    completion_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title