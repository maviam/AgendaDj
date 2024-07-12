from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from forms import ContactForm

# Create your views here.
@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')
	# A ideia é a seguinte: ele vai guardar em form_action, a url a partir do momento que clicamos no send.
	# Ou seja, é a url que está a aceder a view.

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
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
	}
    
    return render(
	    request,
	    'contact/create.html',
		context
	)

@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
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
	}
    
    return render(
	    request,
	    'contact/create.html',
		context
	)

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirmation = request.POST.get('confirmation','no')
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )