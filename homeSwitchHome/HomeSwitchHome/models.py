from django.db import models

# Create your models here.

class Propiedad(models.Model):
	titulo = models.CharField(max_length=30)
	descripcion = models.TextField()
	fotos = models.ImageField(blank=True)
	pais = models.CharField(max_length=20)
	provincia = models.CharField(max_length=20)
	direccion = models.CharField(max_length=40)

	def __str__(self):
		return self.titulo


class Semana(models.Model):
	propiedad = models.ForeignKey('Propiedad', on_delete=models.DO_NOTHING)
	subasta = models.OneToOneField('Subasta', null=True, on_delete=models.DO_NOTHING)
	#reserva = models.OneToOneField('Reserva', null=True, on_delete=models.DO_NOTHING)
	monto_base = models.FloatField()
	costo = models.FloatField()
	numero_semana = models.IntegerField()

class Subasta(models.Model):
	fecha_inicio = models.DsateField(auto_now_add=True)
	fecha_fin = models.DateField(blank=True)

class Postor(models.Model):
	mail = models.EmailField()
	monto_puja = models.FloatField()		

