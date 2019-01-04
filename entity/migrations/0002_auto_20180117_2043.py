# Generated by Django 2.0.1 on 2018-01-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("entity", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="person", name="biography"),
        migrations.AddField(
            model_name="person",
            name="description",
            field=models.TextField(
                blank=True, help_text="A longer-form description.", null=True
            ),
        ),
    ]
