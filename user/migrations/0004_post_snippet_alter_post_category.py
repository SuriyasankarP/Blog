# Generated by Django 4.1.1 on 2022-09-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_category_name_alter_post_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to view post....', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Uncategory', max_length=255),
        ),
    ]