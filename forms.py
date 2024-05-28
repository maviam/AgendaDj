from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                    'class': 'classe-a classe-b',
                    'placeholder': 'Terceira forma de trabalhar com widgets'
                }
        ),
        label = 'Primeiro nome',
        help_text='Texto de ajuda para o utilizador sobre o campo'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Escreva aqui' 
        # })
    class Meta:
        model = Contact
        fields = ('first_name','last_name','phone',)
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs= {
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui'
        #         }
        #     )
        # }
    
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