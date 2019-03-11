from django.shortcuts import render, redirect, reverse
from .models import Link
from .forms import NewLink
import uuid
import qrcode
import io
import base64
from urlshort import settings


def url_redirect(request, path):

    url = Link.objects.filter(path=path).first()
    if not url:
        return render(request, 'links/redirect_failed.html', {'path': path})
    return redirect(url.destination)


def links_dashboard(request):
    root = request.build_absolute_uri()

    links = []

    if request.session.get("links", None) == None:
        return redirect(reverse('links:new'))

    for link in request.session["links"][::-1]:
        print("LINK")
        print(link)
        url = root + link
        qr_code = gen_qr_code(url)
        links.append({"url": url, "qr_code": qr_code})


    return render(request, 'links/new_success.html', {'links': links})


def new_link(request):
    if request.method == 'POST':
        form = NewLink(request.POST)

        if form.is_valid() or settings.DEBUG:

            dest = form.cleaned_data["destination"]  # get the url they typed
            # find any objects with that url
            l = Link.objects.filter(destination=dest).first()

            path = str(uuid.uuid4())[:8]
            if l is None:  # if short url does not exit
                while Link.objects.filter(path=path).first() is not None:
                    path = str(uuid.uuid4())[:8]

                l = Link.objects.create(pk=uuid.uuid4(), destination=dest, path=path)
                l.save()

            if request.session.get("links", None) == None:
                request.session["links"] = []
            request.session["links"].append(path)

        return redirect(reverse('links:dash'))
    else:
        form = NewLink()

    return render(request, 'links/new_link.html', {'form': form})

def gen_qr_code(url):
    img = qrcode.make(url, error_correction=qrcode.constants.ERROR_CORRECT_M)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    img_base64 = "data:image/png;base64," + base64.b64encode(img_byte_arr).decode()

    return img_base64
