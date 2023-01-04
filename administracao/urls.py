from django.urls import path, include
from django.urls.base import reverse_lazy
from .views import servico_views, usuario_views
from django.contrib.auth import views as auth_views


urlpatterns = [   
    path('servicos/listar', servico_views.listar_servicos, name='listar-servicos'),
    path('servicos/cadastrar', servico_views.cadastrar_servico, name='cadastrar-servico'),
    path('servicos/editar/<int:id>', servico_views.editar_servico, name='editar-servico'),
    path('usuarios/listar', usuario_views.listar_usuarios, name='listar-usuarios'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario, name='cadastrar-usuario'),
    path('usuarios/editar/<int:id>', usuario_views.editar_usuario, name='editar-usuario'),
    path('login', auth_views.LoginView.as_view(), name='logar-usuario'),
    path('logout', auth_views.LogoutView.as_view(), name='deslogar-usuario'),
    path('alterar-senha', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('listar-usuarios')), name='alterar-senha'),
    path('resetar-senha', auth_views.PasswordResetView.as_view(),
        name='resetar-senha'),
    path('resetar-senha/sucesso', auth_views.PasswordResetDoneView.as_view(), 
        name='resetar-senha-sucesso'),
    path('resetar-senha/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(), 
        name='resetar-senha-confirmar'),
    path('resetar-senha/feito', auth_views.PasswordResetDoneView.as_view(), 
        name='resetar-senha-feito'),
]
