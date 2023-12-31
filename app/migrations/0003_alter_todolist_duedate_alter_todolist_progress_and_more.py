# Generated by Django 4.2.5 on 2023-09-28 08:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_todolist_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='dueDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='progress',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='taskName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
