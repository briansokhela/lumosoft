from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title