from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone'
    ordering = ('-first_name',)
    # list_filter = ('created_date',) # Aparece à direita algumas possibilidades de filtros
    search_fields = ('first_name','phone',) # Adiciona uma campo de pesquisa
    list_per_page = 10 # Número de registos por página
    list_max_show_all = 200 # Máximo de registos em uma página
    list_editable = ('last_name',) # Lista de campos editáveis
    list_display_links = ('first_name',) # Campo com hierpligação direta para a edição do contato

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',) 