# Generated by Django 4.1 on 2022-08-23 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_profilebiogram_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilelink',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/avatars/% Y/% m/% d/'),
        ),
    ]
