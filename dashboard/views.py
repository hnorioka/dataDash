from django.shortcuts import render
from django.http import HttpRequest, request, response
from .models import DataValue


def index(request):
        dt2 = []
        dy2 = []
        values = DataValue.objects.all()
        for i in values:
                dt2.append(i.value)
                dy2.append(i.day)
        return render(request, 'index.html', {'dt2': dt2, 'dy2': dy2})
        


#labels - do mesmo jeito dos dt 
