from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def index(request):
    return render(request, 'table/index.html')

def result(request):
    if request.method == 'POST':
        number = int(request.POST['number'])
        table = [(number, i, number * i) for i in range(1, 11)]
        return render(request, 'table/result.html', {'number': number, 'table': table})
    else:
        return render(request, 'table/index.html')
