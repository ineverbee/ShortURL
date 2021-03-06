# Generated by Django 3.0.10 on 2020-09-08 20:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200905_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='custom_url',
        ),
        migrations.AddField(
            model_name='shorturl',
            name='new_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='url',
            field=models.URLField(max_length=300, unique=True),
        ),
    ]
