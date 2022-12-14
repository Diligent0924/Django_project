# Generated by Django 4.0.4 on 2022-09-12 14:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articlemodel_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='update_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='release_date',
            field=models.DateField(auto_now=True),
        ),
    ]
