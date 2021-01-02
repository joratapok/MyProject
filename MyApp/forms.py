from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from MyApp.models import Comments, Profile, Links

from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', )


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

class LinkForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Links
        fields = ('description', 'link' )
        widgets = {

            'description': forms.TextInput(attrs={'class': 'special'}),
            'link': forms.TextInput(attrs={'class': 'special'})
        }

class EditUserForm(ModelForm):

    class Meta:
        model = User
        # fields = UserCreationForm.Meta.fields + ('photo', )
        fields = ('first_name', 'last_name', 'username' )

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'country')