# Generated by Django 2.1.4 on 2019-01-01 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcase',
            name='name',
        ),
    ]