from django.db import models

# Register your models here
class Job(models.Model):

    job_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
