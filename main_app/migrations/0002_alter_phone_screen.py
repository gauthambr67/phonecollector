# Generated by Django 4.1.6 on 2023-02-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='screen',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
