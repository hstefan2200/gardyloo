from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/home.html', {'title':'JuanaKnow'})





def learn(request):
    return render(request, 'main/learn.html')


def about(request):
    return render(request, 'main/about.html', {'title':'About'})