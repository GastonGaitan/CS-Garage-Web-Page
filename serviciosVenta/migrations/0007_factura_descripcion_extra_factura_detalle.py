# Generated by Django 4.1.7 on 2023-02-27 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosVenta', '0006_remove_factura_auto_vendido_remove_factura_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='descripcion_extra',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='factura',
            name='detalle',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
