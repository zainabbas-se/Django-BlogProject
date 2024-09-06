# Generated by Django 4.2.15 on 2024-09-02 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]