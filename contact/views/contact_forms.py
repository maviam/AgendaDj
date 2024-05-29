from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
from django.urls import reverse
from forms import ContactForm




# Create your views here.
def create(request):
    form_action = reverse('contact:create')
	# A ideia é a seguinte: ele vai guardar em form_action, a url a partir do momento que clicamos no send.
	# Ou seja, é a url que está a aceder a view.
 
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        context = {
		    'form': form,
            'form_action': form_action,
	    }
        
        if form.is_valid():
            # print('O formulário não contém erros')
            # contact = form.save(commit=False)
            # contact.show = False
            # contact.save()
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)
    
        return render(
	        request,
	        'contact/create.html',
		    context
	    )
    
    context = {
		'form': ContactForm(),
        # 'form_action': form_action
	}
    
    return render(
	    request,
	    'contact/create.html',
		context
	)

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
 
    if request.method == 'POST':
        form = ContactForm(data=request.POST, instance=contact)
        context = {
		    'form': form,
            'form_action': form_action,
	    }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)
    
        return render(
	        request,
	        'contact/create.html',
		    context
	    )
    
    context = {
		'form': ContactForm(instance=contact),
        # 'form_action': form_action
	}
    
    return render(
	    request,
	    'contact/create.html',
		context
	)