# Generated by Django 4.2.7 on 2023-11-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_cartaporte_numero_alter_cartaporte_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartaporte',
            name='fecha_emision',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='conductor',
            name='fecha_nacimiento',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='manifiesto',
            name='fecha_emision',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]