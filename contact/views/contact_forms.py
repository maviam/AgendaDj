from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
from forms import ContactForm




# Create your views here.
def create(request):
    if request.method == 'POST':
        context = {
		    'form': ContactForm(data=request.POST)
	    }
    
        return render(
	        request,
	        'contact/create.html',
		    context
	    )
    
    context = {
		'form': ContactForm()
	}
    
    return render(
	    request,
	    'contact/create.html',
		context
	)