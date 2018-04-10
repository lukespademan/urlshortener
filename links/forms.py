from django import forms


class NewLink(forms.Form):
    destination = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control'}))
