# Generated by Django 2.0.7 on 2019-01-17 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managment_system', '0016_comment_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]