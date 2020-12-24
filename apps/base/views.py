"""Views for the base app"""

from django.shortcuts import render

import sys
import os
sys.path.append(f"{os.path.abspath(os.getcwd())}/source/")  

''' Algorithm '''

from apps.base.src.aux import handleAlgorithmWithDataset

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

    result_list = handleAlgorithmWithDataset(algorithm, dataset)
    print(f"Result is {result_list}, algorithm is {algorithm}, dataset is {dataset}")

    if result_list == []:
        result_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    context = {
        "algorithm": algorithm,
        "dataset": dataset,
        "listOfResults": result_list,
    }

    return render(request, 'result.html', context=context)
