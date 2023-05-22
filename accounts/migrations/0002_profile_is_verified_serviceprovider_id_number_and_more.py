# Generated by Django 4.2.1 on 2023-05-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='id_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='id_picture',
            field=models.ImageField(null=True, upload_to='id_pictures'),
        ),
    ]