# Generated by Django 4.1.3 on 2022-11-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_frog_delete_tumbled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frog',
            name='size',
            field=models.CharField(default='V', max_length=10),
        ),
    ]
