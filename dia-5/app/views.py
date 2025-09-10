from django.shortcuts import render
from django.views.generic import FormView, ListView, DeleteView, DetailView
from .models import ViaCepModel
from .forms import EnderecoForm
from django.urls import reverse_lazy
import requests

def home(request):
    return render(request, 'home.html')

class viaCepFormView(FormView):
    template_name = 'buscar_cep.html'
    form_class = EnderecoForm
    success_url = '/'

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if response.status_code == 200:
            data = response.json()
            endereco_objeto, created = ViaCepModel.objects.get_or_create(
                cep=cep,
                defaults={
                    'rua': data.get('logradouro', ''),
                    'bairro': data.get('bairro', ''),
                    'cidade': data.get('localidade', ''),
                    'estado': data.get('uf', '')
                }
            )
            enderecos = ViaCepModel.objects.all()
            return render(self.request, self.template_name, {
                'form': form,
                'endereco_objeto': endereco_objeto,
                'enderecos': enderecos
                })

class ViaCepListView(ListView):
    model = ViaCepModel
    template_name = 'list.html'
    context_object_name = 'enderecos'

class ViaCepDetailView(DetailView):
    model = ViaCepModel
    template_name = 'detail.html'
    context_object_name = 'endereco_objeto'

class ViaCepDeleteView(DeleteView):
    model = ViaCepModel
    template_name = 'delete.html'
    success_url = reverse_lazy('home')