# Generated by Django 4.0.4 on 2022-09-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_commentmodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='variety',
            field=models.CharField(choices=[('Backjoon', 'Backjoon'), ('SWEA', 'SWEA'), ('Programmers', 'Programmers'), ('else', 'else')], max_length=30),
        ),
    ]
