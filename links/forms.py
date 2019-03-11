from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class NewLink(forms.Form):
    destination = forms.URLField(widget=forms.URLInput(attrs={'class': 'mdl-textfield__input'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
