# Generated by Django 3.2.9 on 2022-06-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
