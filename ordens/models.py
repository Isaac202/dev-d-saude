from django.db import models
from servicos.models import Sercico
from users.models import Usuario

# Create your models here.

class Ordens(models.Model):
    user_id = models.CharField(max_length=20,blank=True,null=True)
    servico = models.ForeignKey(Sercico,on_delete=models.CASCADE, blank=True, null=True)
    proficional = models.ForeignKey(Usuario,on_delete=models.CASCADE, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data_created = models.DateField(auto_now_add=True)
    criado_por = models.CharField(max_length=25, blank=True, null=True)
