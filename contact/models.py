from django.db import models
from django.utils import timezone

# Create your models here.

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

class Contact(models.Model):
    first_name = models.CharField(max_length=20) # string
    last_name = models.CharField(max_length=20) 
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=100, blank=True) # Permite deixar o campo vazio
    # CharField é um campo de preenchimento obrigatório
    created_date = models.DateTimeField(default=timezone.now)
    # Não esquecer de ir a settings.py e alterar o LANGUAGE_CODE para 'pt-pt'
    # e o TIMEZONE para 'Europe/Lisbon'
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'
    
    
    