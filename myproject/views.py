from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def members(request):
    return render(request, 'index.html')
