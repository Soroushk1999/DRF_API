from django.shortcuts import render


def index(request):
    return render(request, 'base/base.html')


def under_construction(request):
    return render(request, 'base/under_construction.html')
