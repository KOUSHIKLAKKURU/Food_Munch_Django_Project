# Generated by Django 4.1.7 on 2023-05-06 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fhsapp', '0009_alter_order_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set(),
        ),
    ]
