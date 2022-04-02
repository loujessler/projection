# from multiprocessing import context
from django.shortcuts import render
from .models import Frame
# from django.http import HttpResponse

def home_page(request):
    frames = Frame.objects.all()
    context = {'frames': frames}
    return render(request, 'home_page.html', context)