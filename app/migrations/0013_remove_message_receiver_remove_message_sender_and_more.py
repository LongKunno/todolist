# Generated by Django 4.2.5 on 2023-10-09 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_message_receiver_alter_message_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]