# Generated by Django 3.2.9 on 2021-12-16 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_reviews_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='name',
        ),
    ]