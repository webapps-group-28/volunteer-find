# Generated by Django 2.2.1 on 2019-06-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='hours',
            new_name='hours_educational',
        ),
        migrations.AddField(
            model_name='profile',
            name='hours_environmental',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='hours_social',
            field=models.IntegerField(default=0),
        ),
    ]
