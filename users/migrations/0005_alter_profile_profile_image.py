# Generated by Django 3.2.9 on 2022-05-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220516_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/user-default.jpg', null=True, upload_to='profiles/'),
        ),
    ]
