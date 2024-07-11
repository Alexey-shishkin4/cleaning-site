from django.shortcuts import render
# Create your views here.


def success(request):
    context = {}
    return render(request, 'success.html', context)