# Generated by Django 4.1.7 on 2023-05-23 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactName', models.CharField(blank=True, max_length=100, null=True)),
                ('contactEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('contactSubject', models.CharField(blank=True, max_length=100, null=True)),
                ('contactMessage', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
