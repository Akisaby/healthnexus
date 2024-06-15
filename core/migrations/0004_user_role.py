# Generated by Django 5.0.3 on 2024-05-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]
