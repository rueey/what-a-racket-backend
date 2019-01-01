from django.db import models
from django.utils import timezone

# Create your models here.
class Testcase(models.Model):
    name = models.CharField(max_length=50, default='untitled', blank=True)
    testcase_id = models.CharField(max_length=400, default='')
    testcase_vals = models.CharField(max_length=400, default='')
    generated_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_recent(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=7)
