# Generated by Django 3.2.5 on 2021-08-01 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ebook',
            old_name='price',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='ebook',
            old_name='cover',
            new_name='video',
        ),
    ]
