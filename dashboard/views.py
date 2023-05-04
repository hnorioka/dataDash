from django.shortcuts import render
from django.http import HttpRequest, request, response
# Create your views here.

dt2 = [
        15,
        21,
        18,
        243,
        239,
        92,
        14,
]

def index(request):
    return render(request, 'index.html', {'dt2': dt2})


