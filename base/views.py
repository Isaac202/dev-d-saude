from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from users.models import Usuario

# Create your views here.
@login_required(login_url='/users/login_user/')
def home(request):
    user = list(Usuario.objects.filter(id = request.user.id).values('criado_por'))
    print(user[0]['criado_por'])
    #user = request.user.id
    #usere = list(Usuarios.objects.filter(id=user).values('empresa'))
    #empresa = usere[0]['empresa']
    #print(user, )
    if request.method == "POST":
        print(request.POST)
        return JsonResponse({'status':1})

    print(request.build_absolute_uri())   
    return render(request,'admin/index.html')