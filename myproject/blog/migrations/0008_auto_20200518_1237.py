# Generated by Django 3.0.2 on 2020-05-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200518_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
