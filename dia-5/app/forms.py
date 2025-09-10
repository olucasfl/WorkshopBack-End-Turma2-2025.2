from django import forms
from .models import ViaCepModel

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = ViaCepModel
        fields = ['cep']

        labels = {
            'cep': 'CEP',
        }
        widgets = {
            'cep': forms.TextInput(attrs={'placeholder': 'Digite o CEP'}),
        }