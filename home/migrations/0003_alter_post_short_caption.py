# Generated by Django 4.1.4 on 2022-12-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_short_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short_caption',
            field=models.TextField(default=' ', max_length=400),
        ),
    ]