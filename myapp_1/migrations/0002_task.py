# Generated by Django 4.2 on 2023-04-21 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp_1.proyect')),
            ],
        ),
    ]
