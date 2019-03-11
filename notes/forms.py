from django import forms
from .models import Note
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class NewNote(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
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


