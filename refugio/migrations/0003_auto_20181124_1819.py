# Generated by Django 2.1.3 on 2018-11-24 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugio', '0002_auto_20181124_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptante',
            name='mascota_a_adoptar',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='direccion',
            field=models.TextField(max_length=50),
        ),
    ]
