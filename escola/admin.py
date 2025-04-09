from django.contrib import admin
from escola.models import Aluno, ResponsavelAluno, Professor, Turmas

class TurmasAdmin(admin.ModelAdmin):
    list_display = ('sala', 'padrinho', 'representante', 'vice_representante', 'itinerario', 'turma')
    list_display_links = ('sala', 'padrinho', 'representante', 'vice_representante', 'itinerario', 'turma')
    search_fields = ('itinerario', 'turma')
    list_filter = ('itinerario', 'turma')

class ResponsaveisAdmin(admin.ModelAdmin):
    list_display = ('name_responsavel', 'phone_number_responsavel', 'email_responsavel', 'address_responsavel', 'cpf_responsavel', 'birthday_responsavel', 'classes_filhos')
    list_display_links = ('name_responsavel', 'phone_number_responsavel', 'email_responsavel', 'address_responsavel', 'cpf_responsavel', 'birthday_responsavel')
    search_fields = ('name_responsavel','name_responsavel', 'phone_number_responsavel', 'email_responsavel', 'cpf_responsavel')
    list_filter = ('name_responsavel', 'cpf_responsavel', 'classes_filhos')
    
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('name_aluno', 'phone_number_aluno', 'email_aluno', 'address_aluno', 'cpf_aluno', 'birthday_aluno', 'class_aluno')
    list_display_links = ('name_aluno', 'phone_number_aluno', 'email_aluno', 'address_aluno', 'cpf_aluno', 'birthday_aluno', 'class_aluno')
    search_fields = ('name_aluno', 'phone_number_aluno', 'email_aluno', 'address_aluno', 'cpf_aluno', 'birthday_aluno', 'class_aluno')
    list_filter = ('name_aluno', 'cpf_aluno', 'class_aluno')
    
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name_professor', 'phone_number_professor', 'email_professor', 'address_professor', 'cpf_professor', 'birthday_professor', 'subject', 'classes')
    list_display_links = ('name_professor', 'phone_number_professor', 'email_professor', 'address_professor', 'cpf_professor', 'birthday_professor', 'subject', 'classes')
    search_fields = ('name_professor', 'phone_number_professor', 'email_professor', 'address_professor', 'cpf_professor', 'birthday_professor', 'subject', 'classes')
    list_filter = ('name_professor', 'subject', 'classes')
    

admin.site.register(Turmas, TurmasAdmin)
admin.site.register(ResponsavelAluno, ResponsaveisAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)