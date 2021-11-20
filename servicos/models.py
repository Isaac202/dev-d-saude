from django.db import models

# Create your models here.
class Sercico(models.Model):
    nome = models.CharField(max_length=255, blank=True,null=True)
    imagem = models.ImageField(upload_to='imagens/%d/%m/%Y/',null=True, blank=True)
    criado_por = models.CharField(max_length=25, blank=True, null=True)
    
class Horario(models.Model):
    dia = models.CharField(max_length=50, blank=True, null=True)
    hora_inicial = models.CharField(max_length=50, blank=True, null=True)
    hora_final = models.CharField(max_length=50, blank=True, null=True)
    
    
'''class Empresa(models.Model):
    logo = models.ImageField(upload_to='imagens/%d/%m/%Y/',null=True, blank=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=18, null=True, blank=True, unique=True)
    data_created = models.DateField(auto_now_add=True)'''
#modelo desnecessario ate o momento