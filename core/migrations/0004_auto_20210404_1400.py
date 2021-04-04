# Generated by Django 3.1.7 on 2021-04-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_question_musicgenre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='musicgenre',
            field=models.CharField(choices=[('Hiphop', 'Hip-hop'), ('Rap', 'Rap'), ('Jazz', 'Jazz'), ('Techno', 'Techno'), ('R & B', 'R & B'), ('Punk', 'Punk'), ('Rock', 'Rock'), ('Alternative', 'Alternative'), ('Metal', 'Metal'), ('Country', 'Country'), ('Indie', 'Indie'), ('EDM', 'EDM'), ('Booty Bass', 'Booty Bass')], default='Booty Bass', max_length=100),
        ),
    ]
