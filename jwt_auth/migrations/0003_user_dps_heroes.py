# Generated by Django 3.2.4 on 2021-06-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
        ('jwt_auth', '0002_alter_user_sr'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dps_heroes',
            field=models.ManyToManyField(blank=True, max_length=3, related_name='dps_heroes', to='heroes.Hero'),
        ),
    ]