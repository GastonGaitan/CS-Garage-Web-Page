# Generated by Django 4.1.7 on 2023-02-27 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosVenta', '0003_auto_patente_auto_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='id',
        ),
        migrations.AlterField(
            model_name='auto',
            name='dni_anterior_duenio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='serviciosVenta.cliente'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='patente',
            field=models.CharField(default=None, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_cliente', models.CharField(max_length=7)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('auto_vendido', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='serviciosVenta.auto')),
                ('servicio', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='serviciosVenta.servicio')),
            ],
        ),
    ]
