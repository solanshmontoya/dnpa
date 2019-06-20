from django.db import models

class Store(models.Model):
	class Meta:
		verbose_name = 'tienda'
	latitude = models.FloatField('latitud')
	length = models.FloatField('longitud')
	address = models.CharField('dirección', max_length=100)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.address

class Notification(models.Model): 
	class Meta:
		verbose_name = 'notificación'
		verbose_name_plural = 'notificaciones'
	name = models.TextField('nombre', blank=True, null=True)
	image = models.ImageField('imagen', null=True)
	description = models.TextField('descripción', blank=True, null=True)
	users_read_by = models.ManyToManyField(User)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.description	