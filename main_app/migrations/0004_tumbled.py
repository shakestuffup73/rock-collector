# Generated by Django 4.1.3 on 2022-11-08 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_feeding_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tumbled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
            ],
        ),
    ]
