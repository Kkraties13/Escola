from django.contrib import admin
from escola.models import Aluno, Responsavel, Professor

class ResponsaveisAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'phone_number', 'email', 'address', 'cpf', 'birthday')
    list_display_links = ('name', 'last_name', 'phone_number', 'email', 'address', 'cpf', 'birthday')
    search_fields = ('name', 'last_name')
    list_filter = ('name', 'last_name')
    
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('name_aluno', 'last_name_aluno', 'phone_number_aluno', 'email_aluno', 'address_aluno', 'cpf_aluno', 'birthday_aluno', 'class_aluno')
    list_display_lubjs = ('name_aluno', 'last_name_aluno', 'phone_number_aluno', 'email_aluno', 'address_aluno', 'cpf_aluno', 'birthday_aluno', 'class_aluno')
    search_fields = ('name_aluno', 'last_name_aluno', 'phone_number_aluno', 'email_aluno', 'address_aluno', 'cpf_aluno', 'birthday_aluno', 'class_aluno')
    list_filter = ('name_aluno', 'last_name_aluno')
    
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name_professor', 'last_name_professor', 'phone_number_professor', 'email_professor', 'address_professor', 'cpf_professor', 'birthday_professor', 'subject', 'classes')
    list_display_links = ('name_professor', 'last_name_professor', 'phone_number_professor', 'email_professor', 'address_professor', 'cpf_professor', 'birthday_professor', 'subject', 'classes')
    search_fields = ('name_professor', 'last_name_professor', 'phone_number_professor', 'email_professor', 'address_professor', 'cpf_professor', 'birthday_professor', 'subject', 'classes')
    list_filter = ('name_professor', 'last_name_professor')
    

admin.site.register(Responsavel, ResponsaveisAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)