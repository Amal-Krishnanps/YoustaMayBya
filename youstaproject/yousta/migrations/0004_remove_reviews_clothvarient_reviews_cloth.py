# Generated by Django 4.2.7 on 2023-12-21 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yousta', '0003_cloths_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='ClothVarient',
        ),
        migrations.AddField(
            model_name='reviews',
            name='cloth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yousta.cloths'),
        ),
    ]
