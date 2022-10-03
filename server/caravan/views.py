from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
import os
from .models import Post
from .forms import ContactForm
import operator


def home(request):
    cars = Post.objects.all().order_by('body', 'id').values()

    cars_major = list()
    for i in range(0, len(cars), 6):
        cars_major.extend(cars[i: i+3])

    cars_minor = list()
    for i in range(3, len(cars), 6):
        cars_minor.extend(cars[i: i + 3])

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['first_name']
            phone = form.cleaned_data['phone']
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено!')

            return HttpResponseRedirect("/")

    form = ContactForm()
    return render(request, 'caravan/home.html', {'cars_major': cars_major,
                                                 'cars_minor': cars_minor,
                                                 'category': ['Седаны', 'Гибриды', 'Кроссоверы', 'Универсалы', 'Хэтчбеки', 'Внедорожники'],
                                                 'form': form})
