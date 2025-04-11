# Generated by Django 5.1.2 on 2024-12-02 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminjob', '0002_job_address'),
        ('user', '0003_alter_userprofile_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminjob.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
            options={
                'unique_together': {('user', 'job')},
            },
        ),
    ]
