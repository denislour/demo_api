from django.http import JsonResponse
from django.shortcuts import render


def test_view(request):
    data = {
        'name': 'Son',
        'age': '28',
    }
    return JsonResponse(data)
