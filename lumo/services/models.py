from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_description = models.TextField(max_length=200)
    detailed_description = models.TextField()
    icon_class = models.CharField(max_length=50, blank=True, help_text="e.g., 'fas fa-code' for FontAwesome") # Or use an ImageField
    image = models.ImageField(upload_to='services/', blank=True)
    sort_order = models.IntegerField(default=0) # To manually order services

    class Meta:
        ordering = ['sort_order', 'title']

    def __str__(self):
        return self.title