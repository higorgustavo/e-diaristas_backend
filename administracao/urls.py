from django.urls import path, include
from django.urls.base import reverse_lazy
from .views import servico_views, usuario_views, diaria_views
from django.contrib.auth import views as auth_views


urlpatterns = [  
    path('diarias/listar', diaria_views.lista_diarias, name='listar_diarias'),
    path('diarias/<int:diaria_id>/transferir', diaria_views.transferir_pagamento_diaria, name='transferir_pagamento'),
    path('servicos/listar', servico_views.listar_servicos, name='listar_servicos'),
    path('servicos/cadastrar', servico_views.cadastrar_servico, name='cadastrar_servico'),
    path('servicos/editar/<int:id>', servico_views.editar_servico, name='editar_servico'),
    path('usuarios/listar', usuario_views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/editar/<int:id>', usuario_views.editar_usuario, name='editar_usuario'),
    path('login', auth_views.LoginView.as_view(), name='logar_usuario'),
    path('logout', auth_views.LogoutView.as_view(), name='deslogar_usuario'),
    path('alterar-senha', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('listar_usuarios')), name='alterar_senha'),
    path('resetar_senha', auth_views.PasswordResetView.as_view(),
        name='resetar_senha'),
    path('resetar_senha/sucesso', auth_views.PasswordResetDoneView.as_view(), 
        name='resetar_senha_sucesso'),
    path('resetar_senha/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(), 
        name='resetar_senha_confirmar'),
    path('resetar_senha/feito', auth_views.PasswordResetDoneView.as_view(), 
        name='resetar_senha_feito'),
]
