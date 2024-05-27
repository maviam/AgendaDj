from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator

# Create your views here.
def create(request):
    if request.method == 'POST': # QUando enviamos os dados do formulário
        print()
        print(request.method)
        # Para ver na consola que o texto escrito é "pego" pela instrução dentro do print
        print(request.POST.get('first_name')) # first_name foi o nome dado ao input do formulário
    
    context = {
		
	}
    
    # Método GET (quando acedemos a página create,html)
    print()
    print(request.method)
    
    return render(
	    request,
	    'contact/create.html',
		context
	)