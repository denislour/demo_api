from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):

    def get(self, request):
        data = {
            'name': 'Son',
            'age': 28,
        }
        return Response(data)

# def test_view(request):
#     data = {
#         'name': 'Son',
#         'age': '28',
#     }
#     return JsonResponse(data)
