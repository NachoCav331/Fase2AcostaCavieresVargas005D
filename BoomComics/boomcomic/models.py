from django.db import models
from django.urls import reverse  		#redirecciona una url de un libro al browser 
import uuid  							#se utiliza para definir atributos clave (pk)

# Create your models here.

class Tipo(models.Model):
    
	tipoo = models.CharField(max_length=200)
	
	def __str__(self):
		return self.tipoo

class Formato(models.Model):

	formatoo = models.CharField(max_length=50)

	def __str__(self):
		return self.formatoo    


class Comic(models.Model):

	title = models.CharField(max_length=200)
	autor = models.ForeignKey('Autor',on_delete=models.SET_NULL, null=True)

	resumen = models.TextField(max_length=10000)
	isbn = models.CharField('ISBN', max_length=13)
	tipo = models.ManyToManyField(Tipo)
	formato = models.ManyToManyField(Formato)
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('comic-datail', args=[str(self.id)])    

class ComicInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID primario de los comics de la tienda')
	comic = models.ForeignKey('Comic', on_delete=models.SET_NULL, null=True)
	imprimir = models.CharField(max_length=200)
    
	ESTADO_COMIC = (
		
		('p', 'Proximamente'),
		('d', 'Disponible'),
		('a', 'Agotado'),
	)

	estado = models.CharField(
		max_length=1,
		choices=ESTADO_COMIC,
		blank=True,
		default='d',
		help_text='Comic/Manga disponible',
	)

	def __str__(self):
		return f'{self.id} ({self.comic.titulo})'

class Autor(models.Model):

	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)

	class Meta: 
		ordering = ['nombre', 'apellido']

	def get_absolute_url(self):
		return reverse('autor-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.apellido}, {self.nombre}'	    
