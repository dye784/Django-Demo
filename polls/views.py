from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    page_list = [1, 2, 3, 4, 5, 6]
    context = {'page_list': page_list}
    return render(request, 'polls/index.html', context)

def detail(request, page_id):
    return HttpResponse("You're looking at page %s." % page_id)
