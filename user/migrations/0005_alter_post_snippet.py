# Generated by Django 4.1.1 on 2022-09-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_post_snippet_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.TextField(default='Click link above to view post....', max_length=255),
        ),
    ]
