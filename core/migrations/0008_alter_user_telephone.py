# Generated by Django 5.0.6 on 2024-05-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_user_age_alter_user_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
