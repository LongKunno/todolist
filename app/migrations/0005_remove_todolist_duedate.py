# Generated by Django 4.2.5 on 2023-09-28 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_todolist_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='dueDate',
        ),
    ]
