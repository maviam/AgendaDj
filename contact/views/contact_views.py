from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator

# Create your views here.
def index(request):
	contacts = Contact.objects.filter(show=True).order_by('-id')

	paginator = Paginator(contacts, 10)
	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)

	context = {
		'page_obj': page_obj,
		'site_title': 'Contatos -'
	}
	return render(
		request,
		'contact/index.html',
		context
	)

def search(request):
    # search_value = request.GET
    # print(search_value)
    search_value = request.GET.get('q','').strip()
    
    if search_value == '':
        return redirect('contact:index')
    
    # https://docs.djangoproject.com/en/5.0/ref/models/lookups/
    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value)).order_by('-id')
            
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
		'page_obj': page_obj,
		'site_title': 'Contatos -'
	}
    
    return render(
		request,
		'contact/index.html',
		context
	)

def contact(request, contact_id):
	# single_contact = Contact.objects.filter(id=contact_id).first()
	single_contact = get_object_or_404(Contact.objects, id=contact_id,show=True)
	
	context = {
		'contact': single_contact,
		'site_title': f'{single_contact.first_name} {single_contact.last_name} -'
	}
	return render(
	    request,
	    'contact/contact.html',
		context
	)