# Generated by Django 3.1.7 on 2021-04-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210404_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
