# Generated by Django 5.0.1 on 2024-01-22 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_rename_owners_phonenumber_owner_phonenumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='сomplaint',
            old_name='complaint_text',
            new_name='text',
        ),
    ]
