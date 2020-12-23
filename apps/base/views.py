"""Views for the base app"""

from django.shortcuts import render

from .src.coin_change_making import countBottomUp


def home(request):

    list_of_algorithms = ['Coin Change Making', 'Knapsack 01', 'Levenshtein Distance', 'Longest Increasing Subsequence', 'Longest Common Subsequence',
                          'Matrix Chain Multiplication', 'Partition Problem - Dynamic', 'Rod Cutting Problem', 'Shortest Common Super Sequence', 'Work Break Problem']

    context = {}
    context['algorithms'] = list_of_algorithms

    """ Default view for the root """
    return render(request, 'home.html', context)


def report(request):
    ''' Report view '''
    return render(request, 'report.html')


def data(request):
    ''' Data view '''
    return render(request, 'data.html')


def contact(request):
    ''' Contact view '''
    return render(request, 'contact.html')


def about(request):
    ''' About view '''
    return render(request, 'about.html')

def result(request, algorithm, dataset):
    ''' About result '''

    context = {
        "algorithm": algorithm,
        "dataset": dataset,
    }

    return render(request, 'result.html', context=context)
