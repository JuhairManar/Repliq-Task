# Generated by Django 5.0 on 2024-01-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_historicalitems_handover_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalitems',
            name='handover_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalitems',
            name='receive_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='handover_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='receive_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]