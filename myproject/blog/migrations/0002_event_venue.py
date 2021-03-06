# Generated by Django 3.0.2 on 2020-02-18 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Venu Name')),
                ('address', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100, verbose_name='Zip/Post code')),
                ('phone', models.CharField(max_length=100, verbose_name='Contact Number')),
                ('email_address', models.CharField(max_length=19, verbose_name='Email adress')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Event Name')),
                ('event_date', models.CharField(max_length=100, verbose_name='Event date')),
                ('description', models.TextField(max_length=100)),
                ('attendees', models.ManyToManyField(to='blog.Address')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Venue')),
            ],
        ),
    ]
