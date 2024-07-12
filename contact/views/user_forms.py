from django.shortcuts import render, redirect
from forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth # O módulo auth possui todos os métodos associados à autenticação

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    
        if form.is_valid():
            form.save()
            messages.success(request, 'Utilizador registado com sucesso!')
            return redirect('contact:login')
        
        context = {
            'user_action_title': 'Register new user',
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
        'user_action_title': 'Register new user',
        'form': form
    }
    return render(
        request,
        'contact/register.html',
        context
    )

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    
    if request.method != 'POST':
        context = {
            'user_action_title': 'Updating user data',
            'form': form
        }
        return render(
            request,
            'contact/register.html',
            context
        )
    
    form = RegisterUpdateForm(request.POST, instance=request.user)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Dados do utilizador atualizados com sucesso!')
        return redirect('contact:index')
    
    context = {
        'user_action_title': 'Updating user data',
        'form': form
    }
    return render(
        request,
        'contact/register.html',
        context
    )

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
    
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('contact:index')
            # print(user)
        else:
            messages.error(request, 'Login inválido! Veja novamente o utilizador e a senha!')
        context = {
            'form': form
        }
        
        return render(
            request,
            'contact/login.html',
            context
        )
        
    form = AuthenticationForm(request)
    context = {
        'form': form
    }
    return render(
        request,
        'contact/login.html',
        context
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')

