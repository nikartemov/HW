from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .models import Flight


class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class SignupForm(forms.Form):
    login = forms.CharField(label='login', min_length=5, )
    email = forms.CharField(label='email')
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')
    password = forms.CharField(label='password', min_length=8, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='repeat_password', widget=forms.PasswordInput)

    def clean_login(self):
        login = self.cleaned_data['login']
        if User.objects.filter(username=login):
            raise ValidationError('Этот login уже занят')
        return login

    def clean_email(self):
        email = self.cleaned_data['email']
        validate_email(self.cleaned_data['email'])
        if User.objects.filter(email=email):
            raise ValidationError('Этот email уже зарегистрирован')
        return self.cleaned_data['email']

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        if self.cleaned_data.get('password') and self.cleaned_data.get('repeat_password'):
            if self.cleaned_data['password'] != self.cleaned_data['repeat_password']:
                raise ValidationError('Пароли не совпадают')
        return cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['login'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        return user


class AddObject(forms.Form):
    flight_number = forms.CharField(label='Flight_Number', max_length=10)
    airlines = forms.CharField(label='Airlines', max_length=20)
    image = forms.FileField(label='image', required=False, widget=forms.widgets.ClearableFileInput(attrs={
        'accept': 'image/jpeg, image/png, image/gif, image/jpg'
    }))
    description = forms.CharField(label='Description', max_length=100)
    airplane = forms.CharField(label='Airplane', max_length=20)
    departure_airport = forms.CharField(label='Dep_Airport', max_length=3)
    arrival_airport = forms.CharField(label='Arr_Airport', max_length=3)
    cost = forms.CharField(label='Cost', max_length=20)


    def fill_object(self):
        return Flight.objects.create(flight_number=self.cleaned_data['flight_number'],
                                     airlines=self.cleaned_data['airlines'],
                                     description=self.cleaned_data['description'],
                                     airplane=self.cleaned_data['airplane'],
                                     departure_airport=self.cleaned_data['departure_airport'],
                                     arrival_airport=self.cleaned_data['arrival_airport'],
                                     cost=self.cleaned_data['cost'])