# Generated by Django 2.2.3 on 2019-07-05 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0007_auto_20190705_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizationimage',
            old_name='new_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='personimage',
            old_name='new_id',
            new_name='id',
        ),
    ]
