from django import forms
from .models import Password


class SharePassword(forms.Form):
    Choices = (
        ('anonymous', 'Отправить анонимно'),
        ('specified', 'Указать имя'),
    )
    name = forms.CharField(max_length=25, )
    email_from = forms.EmailField()
    email_to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
    anonymity = forms.TypedChoiceField(choices=Choices,
                                       widget=forms.RadioSelect,
                                       coerce=str)


class CreatePassword(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['title', 'psw']
