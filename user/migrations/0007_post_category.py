# Generated by Django 4.1.1 on 2022-09-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(default='uncategory'),
        ),
    ]
