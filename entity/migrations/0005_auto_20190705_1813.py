# Generated by Django 2.2.3 on 2019-07-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0004_auto_20190104_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, unique=True),
        ),
    ]
