# Generated by Django 4.1.5 on 2023-01-31 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='')),
                ('stock', models.IntegerField()),
                ('envio_gratis', models.BooleanField(default=False)),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('U', 'Unisex')], max_length=1)),
                ('marca', models.CharField(max_length=40)),
                ('unidad_talle', models.CharField(choices=[('N', 'Numeros'), ('L', 'Letras')], max_length=1)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.categoria')),
            ],
        ),
    ]
