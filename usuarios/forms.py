from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label= "Nome de Login",
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            attrs={
                "class" : "form-control",
                "style" : "margin-bottom: 5px",
                "placeholder" : "EX.: João Silva"
            }
        ),
    )
    senha = forms.CharField(
        label= "Senha",
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "style" : "margin-bottom: 5px",
                "placeholder" : "EX.: 123joaozinho"
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label= "Nome de Cadastro",
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            attrs={
                "class" : "form-control",
                "style" : "margin-bottom: 5px",
                "placeholder" : "EX.: João Silva"
            }
        ),
    )
    email_cadastro = forms.EmailField(
        label= "Email",
        required= True,
        max_length= 100,
        widget= forms.EmailInput(
            attrs={
                "class" : "form-control",
                "style" : "margin-bottom: 5px",
                "placeholder" : "EX.: joaozinhopereirafunk@gmail.com"
            }
        ),
    )
    senha1 = forms.CharField(
        label= "Senha",
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "style" : "margin-bottom: 5px",
                "placeholder" : "Digite sua senha"
            }
        ),
    )
    senha2 = forms.CharField(
        label= "Senha",
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "style" : "margin-bottom: 5px",
                "placeholder" : "Digite sua senha novamente"
            }
        ),
    )

