
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widgwt=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widgwt=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

        def clean_password(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Password don\'t math.')
            return cd['password2']
