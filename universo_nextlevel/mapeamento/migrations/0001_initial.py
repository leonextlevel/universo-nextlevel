# Generated by Django 3.2.6 on 2022-01-09 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20220102_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32, verbose_name='Nome')),
                ('cenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cenario', verbose_name='Cenário')),
            ],
            options={
                'verbose_name': 'Nação',
                'verbose_name_plural': 'Nações',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32, verbose_name='Nome')),
                ('cenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cenario', verbose_name='Cenário')),
                ('dono', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mapeamento.nacao')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32, verbose_name='Nome')),
                ('tipo', models.CharField(choices=[('metropole', 'Metrópole'), ('cidade', 'Cidade'), ('vila', 'Vila')], max_length=9, verbose_name='Tipo')),
                ('cenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cenario', verbose_name='Cenário')),
                ('dono', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mapeamento.estado')),
            ],
            options={
                'verbose_name': 'Distrito',
                'verbose_name_plural': 'Distritos',
                'ordering': ['nome'],
            },
        ),
    ]