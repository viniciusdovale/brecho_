from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def usuario(request):
	user_id = request.user.id

	return user_id




def complete_dados(request):
	''' verifica se user completou seus dados'''

	from home.models import User_extra

	usuario_id = usuario(request)

	cont_user = User_extra.objects.filter(user_id = usuario_id).count()


	return cont_user


# principal da home
def principal(request):
	#verifica se completou dados
	cont_user = complete_dados(request)
	user = request.user
	

	context = RequestContext(request,
		{'user': user,
		'contador':cont_user,
		})

	# se for 0, significa que precisa completar os dados
	if cont_user == 0 and user.is_authenticated():
		return render_to_response('complete.html', context_instance=context)


	return render_to_response('index.html',
		context_instance=context)


#salva os dados complementares do usuario
def completar_dados(request):
	
	return render_to_response('index.html')

 