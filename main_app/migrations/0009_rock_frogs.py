# Generated by Django 4.1.3 on 2022-11-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_frog_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='rock',
            name='frogs',
            field=models.ManyToManyField(to='main_app.frog'),
        ),
    ]
