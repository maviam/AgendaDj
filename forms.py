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
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        msg = ValidationError(
                    'O primeiro e o último nome devem ser diferentes',
                    code='invalid'
                )
        
        if first_name == last_name:
            self.add_error('first_name',msg)
            self.add_error('last_name',msg)
        
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'O primeiro nome não pode ser ABC',
                    code='invalid'
                )
            )
        
        return first_name
            