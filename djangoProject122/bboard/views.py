from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import Bb
from .forms import OrderForm
import datetime
from whatsappbot import send_info


def bb_index(request):
    bbs = Bb.objects.order_by('-published')
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            answer = ""

            answer += "Услуги: "
            for i in data['service']:
                answer += f'{i}, '
            answer += f'\nЖелаемое время: {data["time"].strftime("%m/%d/%y")}'
            answer += f'\nФИО: {data["name"]}'
            answer += f'\nEmail: {data["email_address"]}'
            answer += f'\nТелефон: {data["phone_number"]}'
            answer += f'\nАдрес: {data["address"]}'
            if data['comment']:
                answer += f'\nКомментарий: {data["comment"]}'
            send_info(str(answer))

            context = {'bbs': bbs, 'form': form}
            return HttpResponseRedirect('/success/')
    else:
        form = OrderForm()
    context = {'bbs': bbs, 'form': form}
    return render(request, 'order.html', context)