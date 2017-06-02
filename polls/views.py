from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    page_list = [1, 2, 3, 4, 5, 6]
    context = {'page_list': page_list}
    return render(request, 'polls/index.html', context)

def detail(request, page_id):
    context = {'page_id': page_id}
    return render(request, 'polls/page.html', context)
