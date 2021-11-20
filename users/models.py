from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from servicos.models import Horario, Sercico


class Endereco(models.Model):
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    logradouro = models.CharField(max_length=500, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    criado_por = models.CharField(max_length=25, blank=True, null=True)


class Usuario(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    imagem = models.ImageField(upload_to='imagens/%d/%m/%Y/',null=True, blank=True)
    status_usuario = models.CharField(max_length=2, blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, blank=True, null=True)
    contato = models.CharField(max_length=18, blank=True, null=True)   
    telefone = models.CharField(max_length=18, blank=True, null=True)  
    cpf = models.CharField(max_length=18, null=False, blank=False, unique=True)
    cnpj = models.CharField(max_length=18, null=True, blank=True, unique=True)
    especialidade_user = models.ManyToManyField(Sercico, blank=True, null=True)
    horarios = models.ManyToManyField(Horario,blank=True, null=True)
    criado_por = models.CharField(max_length=255, blank=True, null=True)

    
    @mark_safe
    def icone(self):
        return f'<img width="30px" src="{self.imagem.url}">'