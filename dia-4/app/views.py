from django.shortcuts import render
from .forms import EnderecoForm
from .models import Endereco
import requests

def home(request):
    return render(request, 'home.html')

def buscar_cep(request):
    form = EnderecoForm(request.GET or None)
    endereco = None

    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if response.status_code == 200:
            data = response.json()
            endereco, created = Endereco.objects.get_or_create(
                cep=cep,
                defaults={
                    'rua': data.get('logradouro', ''),
                    'bairro': data.get('bairro', ''),
                    'cidade': data.get('localidade', ''),
                    'estado': data.get('uf', '')
                }
            )

    return render(request, 'buscar_cep.html', {'form': form, 'endereco': endereco})
