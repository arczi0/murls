# Generated by Django 4.1 on 2022-08-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_profilebiogram_remove_profilelink_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileBiogram',
        ),
        migrations.AddField(
            model_name='profilelink',
            name='biogram',
            field=models.CharField(max_length=350, null=True, verbose_name='Opis...'),
        ),
    ]