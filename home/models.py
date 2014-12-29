from django.db import models

# Create your models here.
class User_extra(models.Model):
	''' tabela de um user criado''' 

	user_id = models.IntegerField('User Id', null = False, blank = False)
	user_nick = models.CharField('User Nick', max_length = 20, null = False, blank = False)
	imagem = models.CharField('Imagem', max_length = 10, null = True, blank = True)
	estado = models.CharField('Estado', max_length = 100, null = True, blank = True)
	cidade = models.CharField('Cidade', max_length = 200, null = True, blank = True)
	altura = models.CharField('Altura', max_length = 10, null = True, blank = True)
	cintura = models.CharField('Cintura', max_length = 10, null = True, blank = True)
	calcado = models.CharField('Calcado', max_length = 200, null = True, blank = True)
	celular = models.CharField('Celular', max_length = 200, null = True, blank = True)
	whatsapp = models.CharField('Whatsapp', max_length = 12, null = True, blank = True)
	email = models.EmailField('Email', max_length = 100, null = True, blank = True)
	facebook = models.CharField('Facebook', max_length = 200, null = True, blank = True)
	instagram = models.CharField('Instagram', max_length = 200, null = True, blank = True)
	user_premium = models.CharField('User_premium', max_length = 200, null = True, blank = True)
	data_expiracao_premium = models.DateField('Data Expire', max_length = 50, null = True, blank = True)

	def __unicode__ (self):
		return self.user_nick