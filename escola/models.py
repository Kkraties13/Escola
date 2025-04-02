from django.db import models
import re

def validador(cpf):

    #Retira apenas os dígitos do CPF, ignorando os caracteres especiais
    cpf = re.sub(r'[^0-9]', '', cpf)

    #Verifica a estrutura do CPF (111.222.333-44)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = 0
  
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if cpf[-2:] != str(digito1) + str(digito2):
        return False
    else:
        return True
        

class Turmas(models.Model):
    TURMAS_CHOICES = (
        "1A", "1º Ano A",
        "1B", "1º Ano B",
        "1C", "1º Ano C",
        "2A", "2º Ano A",
        "2B", "2º Ano B",
        "2C", "2º Ano C",
        "3A", "3º Ano A",
        "3B", "3º Ano B",
        "3C", "3º Ano C",
    )
    
    ITINERARIO_CHOICES = (
        "DS", "Desenvolvimento de Sistemas",
        "CN", "Ciências da Natureza",
        "JG", "Desenvolvimento de Jogos",
    )
    
    sala = models.CharField(max_length=2, verbose_name="Sala")
    padrinho = models.CharField(max_length=50, verbose_name="Nome do Padrinho")
    representante = models.CharField(max_length=50, verbose_name="Nome do Representante")
    vice_representante = models.CharField(max_length=50, verbose_name="Nome do Vice Representante")
    itinerario = models.Choices(ITINERARIO_CHOICES, verbose_name="Itinerário")
    turma = models.Choices(TURMAS_CHOICES, verbose_name="Turma")
    
    def __str__(self):
        return self.turma + "" + self.itinerario 

class ResponsavelAluno(models.Model):
    TURMAS_CHOICES = (
        "1A", "1º Ano A",
        "1B", "1º Ano B",
        "1C", "1º Ano C",
        "2A", "2º Ano A",
        "2B", "2º Ano B",
        "2C", "2º Ano C",
        "3A", "3º Ano A",
        "3B", "3º Ano B",
        "3C", "3º Ano C",
    )
    
    name_responsavel = models.CharField(max_length=50)
    last_name_responsavel = models.CharField(max_length=50)
    phone_number_responsavel = models.CharField(max_length=15, verbose_name="Digite seu número de telefone")
    email_responsavel = models.EmailField(max_length=100, verbose_name="E-Mail do responsavel")
    address_responsavel = models.CharField(max_length=100)
    cpf_responsavel = models.CharField(max_length=11, unique=True)
    birthday_responsavel = models.DateField()
    classes_filhos = models.Choices(TURMAS_CHOICES)
    

    def __str__(self):
        return self.name_responsavel + " " + self.last_name_responsavel
    
class Aluno(models.Model):
    TURMA_CHOICES = (
        "1A", "1º Ano A",
        "1B", "1º Ano B",
        "1C", "1º Ano C",
        "2A", "2º Ano A",
        "2B", "2º Ano B",
        "2C", "2º Ano C",
        "3A", "3º Ano A",
        "3B", "3º Ano B",
        "3C", "3º Ano C",
    )
    
    name_aluno = models.CharField(max_length=50)
    last_name_aluno = models.CharField(max_length=50)
    phone_number_aluno = models.CharField(max_length=15, verbose_name="Digite seu número de telefone")
    email_aluno = models.EmailField(max_length=100, verbose_name="E-Mail do Aluno")
    address_aluno = models.CharField(max_length=100)
    cpf_aluno = models.CharField(max_length=11, unique=True)
    birthday_aluno = models.DateField()
    class_aluno = models.CharField(max_length=2, choices=TURMA_CHOICES)
    
    responsavel = models.ForeignKey(
            ResponsavelAluno, 
            on_delete=models.CASCADE, 
            related_name='alunos', 
            verbose_name="Responsável", 
            null=True, 
            blank=False
        )
    
    contrato = models.OneToOneField(
        on_delete=models.CASCADE,
        related_name='aluno',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name_aluno + " " + self.last_name_aluno + " - " + self.class_aluno
    
class Professor(models.Model):
    TURMAS_CHOICES = (
        "1A", "1º Ano A",
        "1B", "1º Ano B",
        "1C", "1º Ano C",
        "2A", "2º Ano A",
        "2B", "2º Ano B",
        "2C", "2º Ano C",
        "3A", "3º Ano A",
        "3B", "3º Ano B",
        "3C", "3º Ano C",
    )
    
    name_professor = models.CharField(max_length=50)
    last_name_professor = models.CharField(max_length=50)
    phone_number_professor = models.CharField(max_length=15, verbose_name="Digite seu número de telefone")
    email_professor = models.EmailField(max_length=100, verbose_name="E-Mail do Professor")
    address_professor = models.CharField(max_length=100)
    cpf_professor = models.CharField(max_length=11, unique=True)
    birthday_professor = models.DateField()
    subject = models.CharField(max_length=50)
    classes = models.Choices(TURMAS_CHOICES)
    
    def __str__(self):
        return self.name_professor
    
