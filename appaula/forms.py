from django import forms
from .models import Instituicao, Setor, Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'data_nascimento', 'telefone', 'email', 'cep']
        labels = {
            'nome':'Nome',
            'cpf':'CPF',
            'data_nascimento':'Data de Nascimento',
            'telefone':'Telefone',
            'email':'E-Mail',
            'cep':'CEP'
        }
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'cpf':forms.TextInput(attrs={'class':'form-control'}),
            'data_nascimento':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'telefone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'type':'email'}),
            'cep':forms.TextInput(attrs={'class':'form-control'}),            
        }


class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ['nome_fantasia','cnpj']
        labels = {
            'nome_fantasia':'Nome fantasia da instituição',
            'cnpj':'CNPJ da instituição'
        }
        widgets = {
            'nome_fantasia':forms.TextInput(attrs={'class':'form-control','required': 'required'}),
            'cnpj':forms.TextInput(attrs={'class':'form-control'}),                            
        }
        # error_messages = {
        #     'nome_fantasia': {
        #         'required': 'O campo "Nome Fantasia" é obrigatório.',
        #     },
        #     'cnpj': {
        #         'required': 'O campo "CNPJ" é obrigatório.',
        #     },
        # }

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome','email','ramal','instituicao']
        labels = {
            'instituicao':'Nome da Instituição',
            'nome':'Nome do Setor',
            'email':'E-Mail do Setor',
            'ramal':'Ramal do Setor',
        }
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'ramal':forms.TextInput(attrs={'class':'form-control'}),
            'instituicao':forms.Select(attrs={'class':'form-control'}),            
        }