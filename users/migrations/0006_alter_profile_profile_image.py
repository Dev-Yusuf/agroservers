# Generated by Django 3.2.9 on 2022-05-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile/user-default.jpg', null=True, upload_to='profile/'),
        ),
    ]
