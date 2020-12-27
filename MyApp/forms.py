from django import forms

from MyApp.models import Comments


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text', )
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