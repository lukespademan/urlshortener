from django.shortcuts import render, redirect
from .models import Link
from .forms import NewLink

def url_redirect(request, path):

    url = Link.objects.filter(path=path).first()
    if not url:
        return render(request, 'links/redirect_failed.html', {'path': path})
    return redirect(url.destination)

def new_link(request):
    if request.method == 'POST':
        form = NewLink(request.POST)
        
        if form.is_valid():
            dest = form.cleaned_data["destination"]
            l = Link.objects.filter(destination=dest).first()
            if not l:
                l = Link(destination=dest)
                l.save()
            return render(request, 'links/new_success.html', {'short_link': l})
    else:
        form = NewLink()

    return render(request, 'links/new_link.html', {'form': form})

