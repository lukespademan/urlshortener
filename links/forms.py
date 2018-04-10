from django import forms


class NewLink(forms.Form):
    destination = forms.URLField()
