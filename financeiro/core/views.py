from django.shortcuts import render, redirect
from .models import Transacao

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