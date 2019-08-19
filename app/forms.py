from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label = 'Senha', widget = forms.PasswordInput(attrs={'placeholder': 'Senha *'}))
    password2 = forms.CharField(label = 'Confirmação de senha', widget = forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha *'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas devem ser iguais')

        return password2

    def save(self, commit = True):
        user = super(RegisterForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'nome_completo', 'email', 'foto_usuario']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário *'}),
            'nome_completo': forms.TextInput(attrs={'placeholder': 'Nome Completo *'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail *'}),
        }