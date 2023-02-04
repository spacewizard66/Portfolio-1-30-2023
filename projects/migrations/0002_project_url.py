# Generated by Django 3.2.7 on 2021-12-22 22:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
