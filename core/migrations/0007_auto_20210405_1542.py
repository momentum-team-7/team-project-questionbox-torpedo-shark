# Generated by Django 3.1.7 on 2021-04-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210405_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]