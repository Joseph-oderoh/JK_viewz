# Generated by Django 4.0.4 on 2022-05-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picz', '0003_alter_images_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_link',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='images/'),
        ),
    ]
