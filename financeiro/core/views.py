from django.shortcuts import render, redirect, get_object_or_404
from .models import Transacao
import pandas as pd
from django.http import HttpResponse
from datetime import datetime

def home(request):
    transacoes = Transacao.objects.all()

    saldo = 0
    for t in transacoes:
        if t.tipo == 'R':
            saldo += t.valor
        else:
            saldo -= t.valor

    return render(request, 'home.html', {
        'transacoes': transacoes,
        'saldo': saldo
    })


def adicionar(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        valor = float(request.POST['valor'])
        tipo = request.POST['tipo']

        Transacao.objects.create(
            titulo=titulo,
            valor=valor,
            tipo=tipo
        )

        return redirect('/')
    

    return render(request, 'adicionar.html')

def zerar(request):
    Transacao.objects.all().delete()
    return redirect('/')


def deletar(request, id):
    transacao = get_object_or_404(Transacao, id=id)
    transacao.delete()
    return redirect('home') 



#pandas
def exportar(request):
    dados = Transacao.objects.values("titulo", "valor","tipo")
    df = pd.DataFrame(list(dados))

    hoje = datetime.now().strftime('%Y-%m-%d')
    nome =f"TRANSACOES_{hoje}.xlsx"

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename={nome}'

    df.to_excel(response, index=False)

    return response

