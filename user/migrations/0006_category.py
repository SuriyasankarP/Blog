# Generated by Django 4.1.1 on 2022-09-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='uncategory', max_length=255)),
            ],
        ),
    ]
