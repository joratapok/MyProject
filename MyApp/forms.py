from django import forms

from MyApp.models import Comments
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comments
        fields = ('text', 'captcha' )
        widgets = {
            'text': forms.Textarea({
                'placeholder': 'Ваш комментарий', 'width': '100%',
                'height': '100px', 'border-radius': '5px', 'border': 'black 1px solid',
                'resize': 'none'
            })
        }
        labels = {
            'text': ''
        }