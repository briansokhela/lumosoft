from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True)
    service_of_interest = models.ForeignKey('services.Service', on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_addressed = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} ({self.submitted_at.date()})"