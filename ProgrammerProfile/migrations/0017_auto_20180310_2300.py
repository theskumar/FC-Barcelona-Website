# Generated by Django 2.0.3 on 2018-03-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammerProfile', '0016_auto_20180310_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
