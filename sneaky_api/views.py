from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def get_shoes(request):
  if request.method == 'GET':
    