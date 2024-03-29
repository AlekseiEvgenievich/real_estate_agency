# Generated by Django 5.0.1 on 2024-01-18 21:40

from django.db import migrations


def connect_owner_data(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    owner_set = Owner.objects.all()
    for owner in owner_set.iterator():
        flats = Flat.objects.filter(owner=owner.owner)
        owner.flats.set(flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_alter_owner_flats_alter_owner_owner_and_more'),
    ]

    operations = [
        migrations.RunPython(connect_owner_data)
    ]
