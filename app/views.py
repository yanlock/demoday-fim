from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app.forms import RegisterForm
from app.models import Receita, User


def home(request):
    rc = Receita.objects.all()
    print(rc)
    return render(request,'home.html', {'receita': rc})


def cadastro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user = authenticate(
            username = user.username, 
            password = form.cleaned_data['password1']
            )
            login(request, user)
            print(user.foto_usuario)
            return render(request, 'login.html')
    else:
        form = RegisterForm()

    ctx = {'form': form}
    return render(request, 'cadastro.html', ctx)


def do_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            return render(request, 'painel.html')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def do_logout(request):
    logout(request)
    return render(request, 'home.html')

def sobre(request):
    logout(request)
    return render(request, 'sobre.html')

@login_required
def painel(request):

    return render(request, 'painel.html')
    
@login_required
def painel_cadastrar_receita(request):
    if request.method == 'POST':
        try:
            nova_receita = Receita()
            user_id = request.POST['id']
            print(user_id)
            nova_receita.usuario = User.objects.get(id = user_id)
            nova_receita.nome_receita = request.POST['nome_receita']
            nova_receita.receita = request.POST['receita']
            nova_receita.descricao_receita = request.POST['descricao_receita']
            nova_receita.ingredientes = request.POST['ingredientes']
            nova_receita.foto_receita = request.FILES['foto_receita']
            nova_receita.prato = request.POST['prato']
            nova_receita.tipo_prato = request.POST['tipo_prato']

            nova_receita.save()
            print(f'Nova receita cadastrada por: {nova_receita.usuario.username}')
            return render(request, 'cadastrar_receita.html', {'msg': 'Nova receita cadastrada!'})
        except:
            print('Erro ao cadastrar nova receita')
            return render(request, 'cadastrar_receita.html', {'msg': 'Erro ao cadastrar receita'})

    return render(request, 'cadastrar_receita.html')