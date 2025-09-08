dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

def acessarChave():
    try:
        chave = input("Digite a chave que deseja acessar: ")
        return(f"O valor da chave '{chave}' é: {dados[chave]}")
    except KeyError:
        print(f"Erro: A chave '{chave}' não existe no dicionário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

print(acessarChave())