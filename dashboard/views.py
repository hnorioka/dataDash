from django.shortcuts import render
from django.http import HttpRequest, request, response
# Create your views here.

dt2 = [
        7,
        6,
        5,
        4,
        3,
        2,
        1,
]

def index(request):
    return render(request, 'index.html', {'dt2': dt2})


