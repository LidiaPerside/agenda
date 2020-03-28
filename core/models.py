from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento (models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank = True, null= True)
    dataEvento = models.DateTimeField(verbose_name="Data do Evento")
    dataCriacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #se o usuário é deletado, todos os dados relacionados tbm sao


    class Meta:
        db_table = 'evento' #exigindo que a tabela se chame evento

    def __str__(self):
        return self.titulo
