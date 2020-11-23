from django.db import models

# Create your models here.
# Register your models here
class Parts(models.Model):

    parts_name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
