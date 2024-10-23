from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import *


# Create your views here.
def task3_1(request):
    return render(request, 'platform.html')


def task3_2(request):
    Buyers = Buyer.objects.all()
    context = {
        'Buyers': Buyers,
    }
    return render(request, 'services.html', context)


def task3_3(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }
    return render(request, 'games.html', context)


def task3_4(request):
    return render(request, 'cart.html')


def menu(request):
    return render(request, 'menu.html')


def sign_up_by_django(request):
    Buyers = Buyer.objects.all()
    info = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            balance = form.cleaned_data['balance']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:

                user_exists = False
                for buyer in Buyers:
                    if buyer.name == username:
                        user_exists = True
                        break

                if user_exists:
                    info['error'] = f'Пользователь {username} уже существует'
                    return HttpResponse(f"Ошибка, {info['error']}!")
                else:

                    Buyer.objects.create(name=username, balance=balance, age=age)
                    return render(request, 'platform.html')

    else:
        form = ContactForm()
    return render(request, 'registration_page2.html', {'form': form})
