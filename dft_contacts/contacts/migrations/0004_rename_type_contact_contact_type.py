# Generated by Django 4.2.19 on 2025-02-22 15:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0003_alter_contact_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="type",
            new_name="contact_type",
        ),
    ]
