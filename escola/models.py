from django.db import models

class Responsavel(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, verbose_name="Digite seu número de telefone")
    email = models.EmailField(max_length=100, verbose_name="E-Mail do Responsável")
    address = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()

    def __str__(self):
        return self.name
    
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
    
    __str__(self):
        return self.name_professor
    