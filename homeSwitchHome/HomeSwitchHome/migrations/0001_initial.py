# Generated by Django 2.2.1 on 2019-05-13 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('fotos', models.ImageField(upload_to='')),
                ('pais', models.CharField(max_length=20, unique=True)),
                ('provincia', models.CharField(max_length=20, unique=True)),
                ('direccion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Semana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_base', models.FloatField()),
                ('costo', models.FloatField()),
                ('numero_semana', models.IntegerField()),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HomeSwitchHome.Propiedad')),
                ('subasta', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='HomeSwitchHome.Subasta')),
            ],
        ),
    ]
