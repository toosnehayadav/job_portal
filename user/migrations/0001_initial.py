# Generated by Django 5.1.2 on 2024-12-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('age', models.PositiveIntegerField()),
                ('address', models.TextField(default='')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
            ],
        ),
    ]
