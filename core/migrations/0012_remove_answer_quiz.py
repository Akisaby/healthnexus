# Generated by Django 5.0.6 on 2024-05-31 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_user_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='quiz',
        ),
    ]
