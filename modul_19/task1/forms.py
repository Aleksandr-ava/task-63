from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(label="Логин",
                               max_length=30,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Введите логин',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(label="Пароль",
                               min_length=8,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 }))
    repeat_password = forms.CharField(label="Повторите пароль",
                                      min_length=8,
                                      required=True,
                                      widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль',
                                                                        'class': 'form-control',
                                                                        'data-toggle': 'password',
                                                                        'id': 'password',
                                                                        }))

    age = forms.IntegerField(label="Введите свой возраст")

    balance = forms.IntegerField(label="Введите свою сумму")
