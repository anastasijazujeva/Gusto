# Generated by Django 3.2.9 on 2021-12-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_reviews_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
