# Generated by Django 4.0.4 on 2022-07-14 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_alter_channel_names_channel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel_names',
            old_name='Channel_name',
            new_name='channel_name',
        ),
    ]