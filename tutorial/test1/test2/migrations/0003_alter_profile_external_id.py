# Generated by Django 4.2 on 2023-04-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0002_alter_profile_options_alter_profile_external_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='Внешний ID пользователя'),
        ),
    ]