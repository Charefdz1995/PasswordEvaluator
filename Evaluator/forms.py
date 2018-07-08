from django import forms


class form_passwd(forms.Form):
    passwd =forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-lg","placeholder":"password","name":"password","type":"password","value":""}))
