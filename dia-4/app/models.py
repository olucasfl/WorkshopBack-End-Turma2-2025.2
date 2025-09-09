from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f"Rua: {self.rua}, Bairro: {self.bairro}, Cidade: {self.cidade} - Estado: {self.estado}, CEP: {self.cep}"