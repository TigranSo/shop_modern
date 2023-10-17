from django.shortcuts import render
from modern.forms import ContactForm, ContactFormMessage
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


def index(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            try:
                send_mail(
                    f'От {request.user.username}',
                    'Номер телефона: ' + phone ,
                    'shop.modern.com@gmail.com',
                    ['shop.modern.com@gmail.com'],
                    fail_silently=False
                )
                messages.success(request, 'Спасибо за заказ звонка на нашем сайте! Мы получили ваш запрос и свяжемся с вами в ближайшее время по указанному телефону!')
                return HttpResponseRedirect(reverse('index'))
            except BadHeaderError:
                messages.warning(request, 'Ошибка в номере.')
        else:
            messages.warning(request, 'Ошибка валидации формы.')
    else:
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'index.html', {'form': form})


def about(request):
    return render(request, 'about.html')



def contact(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactFormMessage()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactFormMessage(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {from_email}, {request.user.username}', 'Тема: ' + subject + '\n' + 'Текст: ' + message ,
                    'shop.modern.com@gmail.com', ['shop.modern.com@gmail.com'], fail_silently=False)
                messages.success(request, 'Ваше сообщение отправлено!')
                return HttpResponseRedirect(reverse('index'))
            except BadHeaderError:
                messages.warning(request, 'Ошибка в номере.')
        else:
            messages.warning(request, 'Ошибка валидации формы.')
    else:
        return HttpResponseRedirect(reverse('contact'))

    return render(request, 'contact.html', {'form': form})
    



def resultat(request):
    return render(request, 'resultat.html')