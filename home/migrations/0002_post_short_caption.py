# Generated by Django 4.1.4 on 2022-12-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_caption',
            field=models.CharField(default=' ', max_length=400),
        ),
    ]
