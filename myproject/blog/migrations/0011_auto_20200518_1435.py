# Generated by Django 3.0.2 on 2020-05-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200518_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
