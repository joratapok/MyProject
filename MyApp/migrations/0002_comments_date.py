# Generated by Django 3.1.4 on 2020-12-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]