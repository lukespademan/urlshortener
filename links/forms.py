from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class NewLink(forms.Form):
    destination = forms.URLField(widget=forms.URLInput(attrs={'class': 'mdl-textfield__input'}))
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
