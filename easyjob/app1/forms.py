from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as DUserCreationForm

from app1.models import Vakancii, Spheres

User = get_user_model()


class ResumeForm(forms.Form):
    surname = forms.CharField()
    name = forms.CharField()
    age = forms.IntegerField()
    experience = forms.IntegerField()
    about_you = forms.CharField()


class AddVacanciiForm(forms.Form):
    sphere = forms.ModelChoiceField(
        queryset=Spheres.objects.all(),
        empty_label=None,
        to_field_name="id",
        required=True,
        widget=forms.Select()
    )
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


class UserCreationForm(DUserCreationForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(DUserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
