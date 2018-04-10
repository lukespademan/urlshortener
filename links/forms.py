from django import forms


class NewLink(forms.Form):
    destination = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
