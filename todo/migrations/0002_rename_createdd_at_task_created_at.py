# Generated by Django 4.2.2 on 2023-06-23 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='createdd_at',
            new_name='created_at',
        ),
    ]