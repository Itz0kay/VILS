# Generated by Django 4.1.7 on 2023-03-25 17:14

import Contents.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to=Contents.models.nameFile)),
            ],
        ),
    ]
