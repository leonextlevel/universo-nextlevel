# Generated by Django 3.2.6 on 2021-08-31 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.PositiveSmallIntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('profissao', models.CharField(max_length=10, verbose_name='Profissão')),
                ('caracteristica_marcante', models.TextField(verbose_name='Característica Marcante')),
                ('background', models.TextField()),
                ('tendencia', models.CharField(choices=[('LB', 'Leal e Bom'), ('NB', 'Neutro e Bom'), ('CB', 'Caótico e Bom'), ('LN', 'Leal e Neutro'), ('N', 'Neutro'), ('CN', 'Caótico e Neutro'), ('LM', 'Leal e Mau'), ('NM', 'Neutro e Mau'), ('CM', 'Caótico e Mau')], max_length=2, verbose_name='Tendência')),
                ('descricao_fisica', models.TextField(verbose_name='Descrição Física')),
            ],
            options={
                'verbose_name': 'Personagem',
                'verbose_name_plural': 'Personagens',
                'ordering': ['nome'],
            },
        ),
    ]