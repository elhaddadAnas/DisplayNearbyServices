# Generated by Django 4.0.4 on 2022-05-24 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20220523_2011'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
        migrations.RemoveField(
            model_name='image',
            name='Id_Service',
        ),
        migrations.RemoveField(
            model_name='service',
            name='Id_Service',
        ),
        migrations.RemoveField(
            model_name='service',
            name='Score',
        ),
        migrations.AddField(
            model_name='image',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='index.service'),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
