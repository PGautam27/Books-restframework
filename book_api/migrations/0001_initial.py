# Generated by Django 4.0.4 on 2022-08-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('completed_reading', models.BooleanField()),
                ('reading_platform', models.CharField(max_length=100)),
            ],
        ),
    ]
