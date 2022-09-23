from django.db import models

# Create your models here.
class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descricao")
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)
    
class Robos(models.Model):
    numero = models.IntegerField(verbose_name="Numero")
    descricao = models.CharField(max_length=150, verbose_name="Descricao")
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)
    
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    def __str__(self):
        return "{} ({})".format(self.numero, self.campo)