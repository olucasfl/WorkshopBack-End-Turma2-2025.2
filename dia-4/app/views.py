from django.shortcuts import render
from .forms import EnderecoForm
from .models import Endereco
import requests
from django.views.generic import FormView

class viaCepFormView(FormView):
    template_name = 'buscar_cep.html'
    form_class = EnderecoForm
    success_url = '/'

    def form_valid(self, form):
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
            return render(self.request, self.template_name, {'form': form, 'endereco': endereco})
        return super().form_invalid(form)


def home(request):
    return render(request, 'home.html')
