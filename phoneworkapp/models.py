from django.db import models

class phonedetails(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)  # Make it nullable

    def __str__(self):
        return self.name

