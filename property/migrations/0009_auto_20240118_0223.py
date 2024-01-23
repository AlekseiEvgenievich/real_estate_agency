# Generated by Django 5.0.1 on 2024-01-17 23:23

from django.db import migrations
import phonenumbers


def add_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flat_set = Flat.objects.all()
    if flat_set.exists():
        for flat in flat_set.iterator():
            parsed_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
            if phonenumbers.is_valid_number(parsed_number):
                flat.owner_pure_phone = phonenumbers.format_number(
                    parsed_number,
                    phonenumbers.PhoneNumberFormat.E164)
                flat.save()


def remove_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flat_set = Flat.objects.all()
    if flat_set.exists():
        for flat in flat_set.iterator():
            flat.owner_pure_phone = flat.owners_phonenumber
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone_alter_flat_has_balcony'),
    ]

    operations = [
        migrations.RunPython(add_owner_pure_phone, remove_owner_pure_phone),
    ]
