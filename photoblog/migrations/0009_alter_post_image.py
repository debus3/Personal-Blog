# Generated by Django 4.0.3 on 2022-05-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoblog', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='photoblog/static/photoblog/featured_image/%Y/%m/%d/'),
        ),
    ]