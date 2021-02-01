from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('This is dashboard')
    return render(request, 'dashboard/index2.html')