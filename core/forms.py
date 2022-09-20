from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import get_user_model

from core import models

from common.authorization import GROUP_CHOICE


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control',
            }
        )
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'data-toggle': 'password',
                'id': 'password',
                }
            )
        )
    password2 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control',
            'data-toggle': 'password',
            'id': 'password',
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'class': 'form-control top',
            }
        )
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control bottom',
            }
        )
    )   
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'remember_me']


class AddUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                'value': 'thanh',
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
                'value': 'thanh@gmail.com',
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                'value': 'thanh',
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control",
                'value': 'thanh',
            }
        ))
    groups = forms.ChoiceField(
        choices=GROUP_CHOICE,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'groups')


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First name","class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last name","class": "form-control"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Phone","class": "form-control"}))
    citizen_identification = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First name","class": "form-control"}))
    tax_code = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First name","class": "form-control"}))
    license_plates = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First name","class": "form-control"}))
    
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    certificate = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    
    gender = forms.ChoiceField(choices=models.GENDER_CHOICES,widget=forms.Select(attrs={"class": "form-control"}))
    degree = forms.ChoiceField(choices=models.DEGREE_CHOICES,widget=forms.Select(attrs={"class": "form-control"}))
    marital_status = forms.ChoiceField(choices=models.MARITAL_STATUS_CHOICES,widget=forms.Select(attrs={"class": "form-control"}))

    birthday = forms.DateField(widget=forms.TextInput(attrs={"class": "form-control",'id': 'date2','type': "date",'name': "date2"}))

    avatar = forms.ImageField(widget=forms.FileInput(attrs={}))
    class Meta:
        model = models.Profile
        fields = ['first_name', 'last_name', 'phone', 'citizen_identification', 'tax_code', 'license_plates', 'avatar', 'address', 'certificate', 'gender', 'degree', 'marital_status', 'birthday']

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['phone'].required = False
        self.fields['citizen_identification'].required = False
        self.fields['tax_code'].required = False
        self.fields['license_plates'].required = False
        self.fields['address'].required = False
        self.fields['certificate'].required = False
        self.fields['avatar'].required = False
        self.fields['gender'].required = False
        self.fields['degree'].required = False
        self.fields['marital_status'].required = False
        self.fields['birthday'].required = False








