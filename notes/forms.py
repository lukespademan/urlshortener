from django import forms
from .models import Note
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class NewNote(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = Note
        fields = ['title', 'body']

        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control'
                }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
                })
            }
