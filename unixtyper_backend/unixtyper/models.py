from django.db import models

# Create your models here.
class ScrapeData(models.Model):
    # Define your model fields here
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Add more fields as needed

    def __str__(self):
        return self.field1