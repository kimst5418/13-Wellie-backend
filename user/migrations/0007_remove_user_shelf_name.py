# Generated by Django 3.1.2 on 2020-11-11 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_shelf_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shelf_name',
        ),
    ]