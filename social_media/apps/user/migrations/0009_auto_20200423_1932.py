# Generated by Django 3.0.4 on 2020-04-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_userprofile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
