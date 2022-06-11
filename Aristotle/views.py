from django.shortcuts import render

# Create your views here.

def platon(request):
    return render(request, 'hello_world.html', {})
