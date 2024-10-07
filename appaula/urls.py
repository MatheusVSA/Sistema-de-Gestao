from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),    

    # URLs para pessoas
    path('pessoa/cadastrar',views.cadastrar_pessoa, name="cadastrar_pessoa"),
    path('pessoa/alterar/<int:id>/',views.cadastrar_pessoa, name="editar_pessoa"),
    path('pessoa/excluir/<int:id>/',views.excluir_pessoa, name="excluir_pessoa"),
    path('pessoas/',views.listar_pessoas, name='listar_pessoas'),

    # URLs para a instituição
    path('instituicao/novo',views.criar_instituicao, name='criar_instituicao'),
    path('instituicao/alterar/<int:id>/', views.criar_instituicao, name='editar_instituicao'),
    path('instituicao/excluir/<int:id>/', views.excluir_instituicao, name='excluir_instituicao'),
    path('instituicoes/', views.listar_instituicoes, name='listar_instituicoes'),

    # URLs para o Setor
    path('setor/novo', views.criar_setor, name='criar_setor'),
    path('setor/alterar/<int:id>/', views.criar_setor, name='editar_setor'),
    path('setor/excluir/<int:id>/', views.excluir_setor, name='excluir_setor'),
    path('setores/', views.listar_setores, name='listar_setores'),

    # URLs para Lotação 
    path('lotacao/novo', views.criar_lotacao, name='criar_lotacao'),
    path('lotacao/alterar/<int:id>/', views.criar_lotacao, name='editar_lotacao'),
    path('lotacao/excluir/<int:id>/', views.excluir_lotacao, name='excluir_lotacao'),
    path('lotacoes/', views.listar_lotacoes, name='listar_lotacoes'),


]
