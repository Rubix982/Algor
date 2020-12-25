"""Views for the base app"""

from apps.base.src.aux import handleAlgorithmWithDataset
from django.shortcuts import render

import sys
import os
sys.path.append(f"{os.path.abspath(os.getcwd())}/source/")

''' Algorithm '''


def home(request):

    list_of_algorithms = ['Longest Common Subsequence', 'Shortest Common Supersequence', 'Levenshtein Distance', 'Longest Increasing Subsequence', 'Matrix Chain Multiplication',
                          'Knapsack 01', 'Partition Problem', 'Rod Cutting Problem', 'Coin Change Making', 'Work Break Problem']

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

    result_list, total_time_taken = handleAlgorithmWithDataset(algorithm, dataset)

    combined_lists = zip(result_list, total_time_taken)

    if result_list == []:
        result_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    context = {
        "algorithm": algorithm,
        "dataset": dataset,
        "listOfResults": combined_lists,
    }

    return render(request, 'result.html', context=context)
