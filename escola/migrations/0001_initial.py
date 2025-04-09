# Generated by Django 5.2 on 2025-04-09 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_professor', models.CharField(max_length=200)),
                ('phone_number_professor', models.CharField(max_length=15, verbose_name='Telefone do professor')),
                ('email_professor', models.EmailField(max_length=100, verbose_name='E-Mail do Professor')),
                ('address_professor', models.CharField(max_length=100)),
                ('cpf_professor', models.CharField(max_length=11, unique=True)),
                ('birthday_professor', models.DateField()),
                ('subject', models.CharField(max_length=50)),
                ('classes', models.CharField(choices=[('1A', '1º Ano A'), ('1B', '1º Ano B'), ('1C', '1º Ano C'), ('2A', '2º Ano A'), ('2B', '2º Ano B'), ('2C', '2º Ano C'), ('3A', '3º Ano A'), ('3B', '3º Ano B'), ('3C', '3º Ano C')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsavelAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_responsavel', models.CharField(max_length=50)),
                ('phone_number_responsavel', models.CharField(max_length=15, verbose_name='Telefone do responsável')),
                ('email_responsavel', models.EmailField(max_length=100, verbose_name='E-Mail do responsavel')),
                ('address_responsavel', models.CharField(max_length=100)),
                ('cpf_responsavel', models.CharField(max_length=11, unique=True)),
                ('birthday_responsavel', models.DateField()),
                ('classes_filhos', models.CharField(choices=[('1A', '1º Ano A'), ('1B', '1º Ano B'), ('1C', '1º Ano C'), ('2A', '2º Ano A'), ('2B', '2º Ano B'), ('2C', '2º Ano C'), ('3A', '3º Ano A'), ('3B', '3º Ano B'), ('3C', '3º Ano C')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(max_length=2, verbose_name='Sala')),
                ('padrinho', models.CharField(max_length=50, verbose_name='Nome do Padrinho')),
                ('representante', models.CharField(max_length=50, verbose_name='Nome do Representante')),
                ('vice_representante', models.CharField(max_length=50, verbose_name='Nome do Vice Representante')),
                ('itinerario', models.CharField(choices=[('DS', 'Desenvolvimento de Sistemas'), ('CN', 'Ciências da Natureza'), ('JG', 'Desenvolvimento de Jogos')], max_length=2, verbose_name='Itinerario')),
                ('turma', models.CharField(choices=[('1A', '1º Ano A'), ('1B', '1º Ano B'), ('1C', '1º Ano C'), ('2A', '2º Ano A'), ('2B', '2º Ano B'), ('2C', '2º Ano C'), ('3A', '3º Ano A'), ('3B', '3º Ano B'), ('3C', '3º Ano C')], max_length=2, verbose_name='Turma')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_aluno', models.CharField(max_length=200)),
                ('phone_number_aluno', models.CharField(max_length=15, verbose_name='Telefone do aluno')),
                ('email_aluno', models.EmailField(max_length=100, verbose_name='E-Mail do Aluno')),
                ('address_aluno', models.CharField(max_length=100)),
                ('cpf_aluno', models.CharField(max_length=11, unique=True)),
                ('birthday_aluno', models.DateField()),
                ('class_aluno', models.CharField(choices=[('1A', '1º Ano A'), ('1B', '1º Ano B'), ('1C', '1º Ano C'), ('2A', '2º Ano A'), ('2B', '2º Ano B'), ('2C', '2º Ano C'), ('3A', '3º Ano A'), ('3B', '3º Ano B'), ('3C', '3º Ano C')], max_length=2)),
                ('responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='escola.responsavelaluno', verbose_name='Responsável')),
            ],
        ),
    ]
