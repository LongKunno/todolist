# Generated by Django 3.2.7 on 2023-10-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_message_receiver_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
