from django.shortcuts import render

def rickroll(request):
    return render(request, 'rickroll/index.html')
