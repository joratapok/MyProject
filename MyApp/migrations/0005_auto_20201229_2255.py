# Generated by Django 3.1.4 on 2020-12-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='batman.png', upload_to='users/%Y/%m/%d'),
        ),
    ]
