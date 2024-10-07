from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Instituicao, Setor, Pessoa, Lotacao
from .forms import InstituicaoForm, SetorForm, PessoaForm, LotacaoForm

#Metodo para abrir a página da Instituição para Novo cadastro ou Alteração de um existente
def criar_instituicao(request, id=None):
    # Se 'id' for fornecido, buscar a Instituição específica, senão, criar nova
    instituicao = get_object_or_404(Instituicao, pk=id) if id else None
    lista_instituicoes = Instituicao.objects.all()

    if request.method == "POST":
        form = InstituicaoForm(request.POST, instance=instituicao)
        if form.is_valid():
            form.save()
            if instituicao:
                messages.success(request, 'Instituição atualizada com sucesso!')
            else:
                messages.success(request, 'Instituição adicionada com sucesso!')

            return redirect('listar_instituicoes')  # Redirecionar para a view de listagem
    else:
        form = InstituicaoForm(instance=instituicao)

    return render(request, 'appaula/form_instituicao.html', {
        'form': form,
        'lista_instituicoes': lista_instituicoes,
        'instituicao': instituicao
    })

def excluir_instituicao(request, id):
    instituicao = get_object_or_404(Instituicao,pk=id)
    instituicao.delete()
    instituicao=None
    lista_instituicoes=Instituicao.objects.all()
    form = InstituicaoForm(instance=instituicao)
    return render(request, 'appaula/form_instituicao.html', {
        'form': form,
        'lista_instituicoes': lista_instituicoes,
        'instituicao': instituicao
    })
    
#Metodo para listar as instituições cadastradas
def listar_instituicoes(request):
    instituicao = None
    lista_instituicoes = Instituicao.objects.all()
    form = InstituicaoForm(instance=instituicao)
    return render(request, 'appaula/form_instituicao.html', {
        'form': form,
        'lista_instituicoes': lista_instituicoes,
        'instituicao': instituicao})

#Metodo para abrir a página do setor para Novo cadastro ou Alteração de um existente
def criar_setor(request, id=None):
    # Se 'id' for fornecido, buscar o Setor específico, senão, criar um novo
    setor = get_object_or_404(Setor, pk=id) if id else None
    lista_setores = Setor.objects.all()

    if request.method == "POST":
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            if setor:
                messages.success(request, 'Setor atualizado com sucesso!')
            else:
                messages.success(request, 'Setor adicionado com sucesso!')

            return redirect('listar_setores')  # Redirecionar para a view de listagem
    else:
        form = SetorForm(instance=setor)

    return render(request, 'appaula/form_setor.html', {
        'form': form,
        'lista_setores': lista_setores,
        'setor': setor
    })

# Método para excluir um setor existente
def excluir_setor(request, id):
    setor = get_object_or_404(Setor,pk=id)
    setor.delete()
    setor=None
    lista_setores=Setor.objects.all()
    form = SetorForm(instance=setor)
    return render(request, 'appaula/form_setor.html', {
        'form': form,
        'lista_setores': lista_setores,
        'setor': setor
    })

#Metodo para listar os setores cadastrados
def listar_setores(request):
    setor = None
    lista_setores = Setor.objects.all()
    form = SetorForm(instance=setor)
    return render(request, 'appaula/form_setor.html', {
        'form': form,
        'lista_setores': lista_setores,
        'setor': setor})

# Metodo para cadastrar pessoas
def cadastrar_pessoa(request, id=None):
    # Se 'id' for fornecido, buscar o Setor específico, senão, criar um novo
    pessoa = get_object_or_404(Pessoa, pk=id) if id else None
    lista_pessoas = Pessoa.objects.all()

    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            if pessoa:
                messages.success(request, 'Cadrastro atualizado com sucesso!')
            else:
                messages.success(request, 'Cadastro realizado com sucesso!')

            return redirect('listar_pessoas')  # Redirecionar para a view de listagem
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'appaula/cadastro_pessoa.html', {
        'form': form,
        'lista_pessoas': lista_pessoas,
        'pessoa': pessoa
    })

# Método para excluir o cadastro de uma pessoa
def excluir_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa,pk=id)
    pessoa.delete()
    pessoa=None
    lista_pessoas=Pessoa.objects.all()
    form = PessoaForm(instance=pessoa)
    return render(request, 'appaula/cadastro_pessoa.html', {
        'form': form,
        'lista_pessoas': lista_pessoas,
        'pessoa': pessoa
    })

#Metodo para listar as pessoas cadastradas
def listar_pessoas(request):
    pessoa = None
    lista_pessoas = Pessoa.objects.all()
    form = PessoaForm(instance=pessoa)
    return render(request, 'appaula/cadastro_pessoa.html', {
        'form': form,
        'lista_pessoas': lista_pessoas,
        'pessoa': pessoa
    })

#Metodo para criar lotação
def criar_lotacao(request, id=None):
    # Se 'id' for fornecido, buscar o Setor específico, senão, criar um novo
    lotacao = get_object_or_404(Lotacao, pk=id) if id else None
    lista_lotacao = Lotacao.objects.all()

    if request.method == "POST":
        form = LotacaoForm(request.POST, instance=lotacao)
        if form.is_valid():
            form.save()
            if lotacao:
                messages.success(request, 'Lotação atualizada com sucesso!')
            else:
                messages.success(request, 'Lotação realizada com sucesso!')

            return redirect('listar_lotacoes')  # Redirecionar para a view de listagem
    else:
        form = LotacaoForm(instance=lotacao)

    return render(request, 'appaula/form_lotacao.html', {
        'form': form,
        'lista_lotacao': lista_lotacao,
        'lotacao': lotacao
    })

# Metodo para excluir lotações 
def excluir_lotacao(request, id):
    lotacao = get_object_or_404(Lotacao, pk=id)
    lotacao.delete()
    lotacao = None
    lista_lotacao = Lotacao.objects.all()
    form = LotacaoForm(instance=lotacao)
    return render(request, 'appaula/form_lotacao.html', {
        'form': form,
        'lista_lotacao': lista_lotacao,
        'lotacao': lotacao,
    })

# Metodo para listar as lotações 
def listar_lotacoes(request):
    lotacao = None
    lista_lotacao = Lotacao.objects.all()
    form = LotacaoForm(instance=lotacao)
    return render(request, 'appaula/form_lotacao.html', {
        'form': form,
        'lista_lotacao': lista_lotacao,
        'lotacao': lotacao 
    })

# Create your views here.
#chama a pagina index
def index(request):

    return render(request,'appaula/index.html')

#chama a pagina cadastro_pessoa.html
def cadastro_pessoa(request):
    
    return render(request,'appaula/cadastro_pessoa.html')


