# Generated by Django 4.1 on 2022-08-20 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profilelink_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileBiogram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=350, null=True, verbose_name='Opis...')),
            ],
        ),
        migrations.RemoveField(
            model_name='profilelink',
            name='bio',
        ),
    ]
