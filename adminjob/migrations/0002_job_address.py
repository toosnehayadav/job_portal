# Generated by Django 5.1.2 on 2024-12-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminjob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='address',
            field=models.CharField(default='Mumbai', max_length=255, null=True),
        ),
    ]
