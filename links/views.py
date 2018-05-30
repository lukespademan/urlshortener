from django.shortcuts import render, redirect
from .models import Link
from .forms import NewLink
import uuid
import qrcode
import io
import base64


def url_redirect(request, path):

    url = Link.objects.filter(path=path).first()
    if not url:
        return render(request, 'links/redirect_failed.html', {'path': path})
    return redirect(url.destination)


def new_link(request):
    if request.method == 'POST':
        form = NewLink(request.POST)

        if form.is_valid():
            dest = form.cleaned_data["destination"]  # get the url they typed
            # find any objects with that url
            l = Link.objects.filter(destination=dest).first()

            path = str(uuid.uuid4())[:8]
            if l is None:  # if short url does not exit
                while Link.objects.filter(path=path).first() is not None:
                    path = str(uuid.uuid4())[:8]
                l = Link.objects.create(pk=uuid.uuid4(), destination=dest, path=path)
                l.save()

            img = qrcode.make('https://lspade.xyz/l/' + l.path)

            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            img_base64 = "data:image/png;base64," + base64.b64encode(img_byte_arr).decode()

            return render(request, 'links/new_success.html', {'short_link': l, "qr_img": img_base64})
    else:
        form = NewLink()

    return render(request, 'links/new_link.html', {'form': form})

