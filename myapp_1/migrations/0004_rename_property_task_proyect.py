# Generated by Django 4.2 on 2023-04-22 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0003_question_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='property',
            new_name='proyect',
        ),
    ]