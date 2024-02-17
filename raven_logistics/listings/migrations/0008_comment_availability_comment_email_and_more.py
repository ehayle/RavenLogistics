# Generated by Django 5.0.2 on 2024-02-17 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0007_remove_comment_experience_remove_comment_location_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="availability",
            field=models.CharField(default="start date", max_length=60),
        ),
        migrations.AddField(
            model_name="comment",
            name="email",
            field=models.CharField(default="candidate email", max_length=60),
        ),
        migrations.AddField(
            model_name="comment",
            name="license_type",
            field=models.CharField(default="candidate license", max_length=60),
        ),
        migrations.AddField(
            model_name="comment",
            name="location",
            field=models.CharField(default="candidate location", max_length=60),
        ),
        migrations.AddField(
            model_name="comment",
            name="phone",
            field=models.CharField(default="candidate phone number", max_length=60),
        ),
    ]