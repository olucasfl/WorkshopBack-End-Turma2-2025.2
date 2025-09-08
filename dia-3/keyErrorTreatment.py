dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

def key_error_treatment():
    try:
        chave = input("Digite a chave que deseja acessar: ")
        print(f"O valor da chave '{chave}' é: {dados[chave]}")
    except KeyError:
        print(f"A chave '{chave}' não existe no dicionário.")

key_error_treatment()