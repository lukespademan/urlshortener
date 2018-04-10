from django.shortcuts import render

def user_profile(request, name):
    return render(request, 'links/redirect_failed.html', {'path': name})
# Create your views here.
