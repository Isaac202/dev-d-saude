from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from users.models import Usuario
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def create_user_adm(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        cnpj = request.POST['cnpj']
        senha = request.POST['senha']
        user = Usuario.objects.create_user(
                                first_name=nome,
                                username=email,
                                email=email,
                                cnpj=cnpj,
                                cpf=cpf,
                                status_usuario = '1',
                                password=senha,
                                            )
        user.save()
        return redirect('/users/login_user/')
    return render(request,'admin/usuario_add.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['email']
        senha = request.POST['senha']
        print(username, senha)
        user = authenticate( request,username=username, password=senha)
        if user is not None:
            print(username, senha)
            login(request, user)
            print('Logado')
            return redirect('/dashboard/')
    return render(request,'admin/login_user.html')

@login_required(login_url='/users/login_user/')
def logout_user(request):
    logout(request)
    return redirect('/users/login_user/')



# ADCIONAR USARIO COMUN
@login_required(login_url='/users/login_user/')
def usuario(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        wapp = request.POST['wapp']
        cpf = request.POST['cpf']
        tel = request.POST['tel']
        cnpj = request.POST['cnpj']
        senha = request.POST['senha']
        user = Usuario.objects.create_user(first_name=nome,
                                            username=email,
                                            email=email,
                                            cnpj=cnpj,
                                            cpf=cpf,
                                            telefone = tel,
                                            contato= wapp,
                                            status_usuario = '4',
                                            password=senha,
                                            )
        print(user)
        user.save()
        return JsonResponse({'status':1})
       
    usuario = Usuario.objects.all()
    return render(request,'admin/usuario.html',{'usuario':usuario})

@login_required(login_url='/users/login_user/')
def edit_user_admin(request):
    usuario = Usuario.objects.filter(id = request.GET['user_id'])
    print(usuario)
    return render(request,'admin/edit_user_admin.html',{'usuario':usuario})
@login_required(login_url='/users/login_user/')
def edit_user(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        wapp = request.POST['wapp']
        tel = request.POST['tel']
        cnpj = request.POST['cnpj']
        senha = request.POST['senha']
        user = Usuario.objects.filter(email =email).update(first_name=nome,
                                            username=email,
                                            email=email,
                                            contato= wapp,
                                            cnpj=cnpj,
                                            telefone = tel,
                                            cpf=cpf,
                                            )
        u = Usuario.objects.get(email =email)
        if senha != '':
            print(senha)
            u.set_password(senha)
            u.save()
            print(user)
        
        return redirect('/users/usuario/')
@login_required(login_url='/users/login_user/')
def delete_user(request):
    u =Usuario.objects.filter(id = request.GET['user_id']).delete()
    return redirect('/users/usuario/')