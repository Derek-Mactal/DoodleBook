# Generated by Django 2.2.4 on 2021-03-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doodle_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='description',
            field=models.TextField(default='Comment'),
        ),
    ]
