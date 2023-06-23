from django.shortcuts import render, redirect
from ..forms.usuario_forms import CadastroUsuarioForm, EditarUsuarioForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def listar_usuarios(request):
    User = get_user_model()
    usuarios = User.objects.filter(is_superuser=True)
    context = {
        "usuarios": usuarios
    }
    return render(request, "usuarios/listar_usuarios.html", context)


@login_required
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = CadastroUsuarioForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_usuarios')
    else:
        form_usuario = CadastroUsuarioForm()

    context = {
        "form_usuario": form_usuario
    }
    return render(request, "usuarios/form_usuario.html", context)



@login_required
def editar_usuario(request, id):
    User = get_user_model()
    usuario = User.objects.get(id=id)
    form_usuario = EditarUsuarioForm(request.POST or None, instance=usuario)
    if form_usuario.is_valid():
        form_usuario.save()
        return redirect('listar_usuarios')
    else:
        context = {
            "form_usuario": form_usuario
        }
    return render(request, "usuarios/form_usuario.html", context)


# @login_required
# def editar_usuario(request, id):
#     User = get_user_model()
#     usuario = User.objects.get(id=id)
#     form_usuario = EditarUsuarioForm(request.POST or None, instance=usuario)
#     if form_usuario.is_valid():
#         form_usuario.save()
#         return redirect('listar-usuarios')
#     else:
#         context = {
#             "form_usuario": form_usuario
#         }
#     return render(request, "usuarios/editar_usuario.html", context)
