from .models import Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = [
            'username',
            'anons',
            'comment',
            'date'
        ]
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Немного о себе',
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            })
        }
