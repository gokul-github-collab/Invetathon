# Generated by Django 4.2.2 on 2023-08-28 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.TextField(null=True),
        ),
    ]