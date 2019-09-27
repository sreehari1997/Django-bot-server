from django.http import HttpResponse
from .models import Buttoncount
from django.shortcuts import render

def chart(request):
    users = Buttoncount.objects.values()
    context= {'users': users}
    return render(request, 'chart/chart.html', context)