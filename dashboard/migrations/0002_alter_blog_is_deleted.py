# Generated by Django 4.2.15 on 2024-09-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='is_deleted',
            field=models.BooleanField(default=True),
        ),
    ]
