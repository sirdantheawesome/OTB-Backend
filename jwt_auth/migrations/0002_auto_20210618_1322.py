# Generated by Django 3.2.4 on 2021-06-18 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dps1',
            new_name='dps_1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='dps2',
            new_name='dps_2',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='dps3',
            new_name='dps_3',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='support1',
            new_name='support_1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='support2',
            new_name='support_2',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='support3',
            new_name='support_3',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tank1',
            new_name='tank_1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tank2',
            new_name='tank_2',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tank3',
            new_name='tank_3',
        ),
    ]
