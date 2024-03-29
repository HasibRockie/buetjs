# Generated by Django 4.1.4 on 2023-01-29 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_allcomment_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gellery',
            name='caption',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='gellery',
            name='date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='gellery',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gellery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/gellery'),
        ),
    ]
