from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import Bb
from .forms import OrderForm


def bb_index(request):
    bbs = Bb.objects.order_by('-published')
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data['address']
            print(data)
            context = {'bbs': bbs, 'form': form}
            return HttpResponseRedirect('/success/')
    else:
        form = OrderForm()
    context = {'bbs': bbs, 'form': form}
    return render(request, 'order.html', context)