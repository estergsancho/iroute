from django import forms

class LogInUsuarios( forms.Form):
    username = forms.CharField( label='Nombre de usuario', max_length=20)
    password = forms.CharField( widget=forms.PasswordInput, label='Contraseña', max_length=30)


class RegCliente( forms.Form):
    nombre = forms.CharField( label='Nombre', max_length=20)
    apellidos = forms.CharField( label='Apellidos', max_length=40)
    dni = forms.CharField(label = 'DNI', max_length=9)
    nombreUser = forms.CharField(label='Nombre de Usuario', max_length=50)
    password = forms.CharField( widget=forms.PasswordInput, label='Contraseña', max_length=30)
    

