# Generated by Django 2.2.12 on 2022-05-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20220523_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Score',
            field=models.DecimalField(decimal_places=2, max_digits=39),
        ),
    ]