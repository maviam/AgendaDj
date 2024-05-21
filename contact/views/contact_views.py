from django.shortcuts import render, get_object_or_404
from contact.models import Contact

# Create your views here.
def index(request):
	contacts = Contact.objects.filter(show=True).order_by('-id')[0:11]
	context = {
		'contacts': contacts,
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