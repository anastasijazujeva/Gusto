# Generated by Django 3.2.9 on 2021-12-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20211212_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='user',
            field=models.CharField(max_length=150),
        ),
    ]