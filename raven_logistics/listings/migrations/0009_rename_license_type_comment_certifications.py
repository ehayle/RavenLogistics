# Generated by Django 5.0.2 on 2024-02-17 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0008_comment_availability_comment_email_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="license_type",
            new_name="certifications",
        ),
    ]
