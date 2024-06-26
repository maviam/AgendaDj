from django.shortcuts import render, redirect
from forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    
        if form.is_valid():
            form.save()
            messages.success(request, 'Utilizador registado com sucesso!')
            return redirect('contact:index')
        
        context = {
            'form': form
        }
        
        return render(
            request,
            'contact/register.html',
            context
        )
        
    form = RegisterForm()
    messages.info(request,'Bem vindo ao registo de novos utilizadores da nossa app!')
    context = {
        'form': form
    }
    return render(
        request,
        'contact/register.html',
        context
    )