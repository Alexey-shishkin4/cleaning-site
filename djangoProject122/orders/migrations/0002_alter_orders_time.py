# Generated by Django 5.0.6 on 2024-07-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
