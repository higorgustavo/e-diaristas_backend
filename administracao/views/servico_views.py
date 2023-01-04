from django.shortcuts import render, redirect
from ..models import Servico
from ..forms.servico_forms import ServicoForm
from django.contrib.auth.decorators import login_required


@login_required
def listar_servicos(request):
    servicos = Servico.objects.all()
    context = {
        "servicos": servicos
    }
    return render(request, "servicos/listar_servicos.html", context)


@login_required
def cadastrar_servico(request):
    if request.method == "POST":
        form_servico = ServicoForm(request.POST)
        if form_servico.is_valid():
            form_servico.save()
            return redirect('listar-servicos')
    else:
        form_servico = ServicoForm()

    context = {
        "form_servico": form_servico
    }
    return render(request, "servicos/form_servico.html", context)


@login_required
def editar_servico(request, id):
    servico = Servico.objects.get(id=id)
    form_servico = ServicoForm(request.POST or None, instance=servico)
    if form_servico.is_valid():
        servico = form_servico.save(commit=False)
        servico.save()
        return redirect('listar-servicos')
    else:
        context = {
            "form_servico": form_servico
        }
        return render(request, "servicos/form_servico.html", context)
