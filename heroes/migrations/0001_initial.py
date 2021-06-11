# Generated by Django 3.2.4 on 2021-06-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img_large', models.URLField()),
                ('img_banner', models.URLField()),
                ('role', models.CharField(choices=[('DPS', 'dps'), ('TANK', 'tank'), ('SUPPORT', 'support')], default='DPS', max_length=10)),
            ],
        ),
    ]
