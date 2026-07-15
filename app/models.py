from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100,blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_year = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name