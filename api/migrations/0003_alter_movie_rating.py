# Generated by Django 4.1.2 on 2022-10-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
