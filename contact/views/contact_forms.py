from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name','last_name','phone',)
    
    def clean(self):
        # Para mostrar que a classe tem acesso aos dados dos campos antes da submissão ...
        cleaned_data = self.cleaned_data # Guarda os valores inseridos em um dicionário
        print(cleaned_data)
        # Vamos simular erros
        self.add_error(
			None,
			ValidationError(
				'Dados em falta ou inválidos',
				code='invalid'
			)
		)
        # Vamos simular outro erro
        self.add_error(
			None,
			ValidationError(
				'Nova mensagem de erro',
				code='invalid'
			)
		)
        return super().clean()

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