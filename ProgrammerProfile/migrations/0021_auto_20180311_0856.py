# Generated by Django 2.0.3 on 2018-03-11 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammerProfile', '0020_auto_20180310_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]