# Generated by Django 5.0.1 on 2024-01-24 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_rename_owner_owner_user_alter_flat_liked_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда создано объявление'),
        ),
    ]
