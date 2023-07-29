from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato


# -------------------------- REGISTER ------------------------------
def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    # PEGANDO OS VALORES INSERIDOS NO CADASTRO E JOGANDO NA VARIAVEL COM MESMO NOME DO CAMPO
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    # Fazendo checagens para validações todos os campos devem ser preenchidos:
    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Deve preencher todos os campos.')
        return render(request, 'accounts/register.html')

    # Fazendo validaçãoo de email:
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/register.html')

    # Regras para a Senha:
    if len(senha) < 6:
        messages.error(request, 'Senha necessita de no minímo 6 caracteres.')
        return render(request, 'accounts/register.html')
    if senha != senha2:
        messages.error(request, 'Divergêcia na senha, tente novamente!.')
        return render(request, 'accounts/register.html')

    # Regras para quantidade de caracteres de Usuario:
    if len(usuario) < 6:
        messages.error(request, 'Usuario necessita de no minímo 6 caracteres.')
        return render(request, 'accounts/register.html')

    # Verificando se o usuario e o email ja existe:
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuario já existe.')
        return render(request, 'accounts/register.html')
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe.')
        return render(request, 'accounts/register.html')

    # Salvando o cadastro:
    messages.success(request, 'Registrado com sucesso! Faça login.')
    user = User.objects.create_user(first_name=nome,
                                    last_name=sobrenome,
                                    email=email,
                                    username=usuario,
                                    password=senha)
    user.save()
    return redirect('login')


# -------------------------- LOGIN ------------------------------
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    # PEGANDO OS VALORES INSERIDOS NO LOGIN E JOGANDO NA VARIAVEL COM MESMO NOME DO CAMPO
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    # Checando se o usuario vai autenticar:
    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request, 'Usuário ou senha inválido.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com sucesso!')
        return redirect('dashboard')

# -------------------------- DASHBOARD ------------------------------
# Usando um decorador para se o usuario chegar no dashbord e nao tiver logado, ele volta pro login.
@login_required(redirect_field_name='login')
def dashboard(request):
    # Recebendo os dados do form:
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    # Se o form não for valido
    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário. Tente novamente.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    # Regra da descrição
    descricao = request.POST.get('descricao')
    if len(descricao) < 5:
        messages.error(request, 'Descrição necessita ser maior que 5 caracteres.')
        
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    # Salvando e Enviando novo contato:
    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
    return redirect('index')











# -------------------------- LOGOUT ------------------------------
# LOGOUT PARA SAIR DA SUA CONTA
def logout(request):
    auth.logout(request)
    # A partir do momento que desloga e vai para pagina de login
    return redirect('login')
