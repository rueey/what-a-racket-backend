from django.db import models
from django.utils import timezone

# Create your models here.
class Testcase(models.Model):
    testcase_id = models.CharField(max_length=400, default='')
    testcase_vals = models.TextField(max_length=400, default='')
    generated_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_recent(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=7)
