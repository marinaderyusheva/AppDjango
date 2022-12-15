from django import forms
from django.core.exceptions import ValidationError

from app1.models import Vakancii


class ResumeForm(forms.Form):
    surname = forms.CharField()
    name = forms.CharField()
    age = forms.IntegerField()
    experience = forms.IntegerField()
    about_you = forms.CharField()

class AddVacanciiForm(forms.Form):
    sphere = forms.CharField()
    name_vacancii = forms.CharField()
    zadacha = forms.CharField()
    about_vacancii = forms.CharField()

class AddVakancii(forms.ModelForm):
        class Meta:
            model = Vakancii
            fields = ('title_vakancii', 'sphere', 'about_vakancii',)
            # fields ='__all__'
            widgets = {
                'title_vakancii': forms.TextInput(attrs={'class': 'form - input'}),
                'sphere': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
                'about_vakancii': forms.TextInput(attrs={'class': 'form - input'}),
            }

        def clean_title_vakancii(self):
            title_vakancii = self.cleaned_data['title_vakancii']
            if len(title_vakancii) > 50:
                raise ValidationError('Длина превышает 50 символов')
            return title_vakancii
