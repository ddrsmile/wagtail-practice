from django.shortcuts import render

def home(request):
    return render(request, 'joeyliu/home.html', {'name':'JOEYLIU'})
