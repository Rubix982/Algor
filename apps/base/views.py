"""Views for the base app"""

from django.shortcuts import render


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')


def report(request):
    ''' Report view '''
    return render(request, 'base/report.html')


def data(request):
    ''' Data view '''
    return render(request, 'base/data.html')


def contact(request):
    ''' Contact view '''
    return render(request, 'base/contact.html')

def about(request):
    ''' About view '''
    return render(request, 'base/about.html')
