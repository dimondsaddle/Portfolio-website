# Generated by Django 2.2.24 on 2021-11-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211108_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
