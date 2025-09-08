def somar(a, b):

    try:
        return a + b

    except ValueError:
        return "Erro: Ambos os valores devem ser números."
    except TypeError:
        return "Erro: Tipo de dado inválido."
    except ZeroDivisionError:
            return "Erro: Divisão por zero não é permitida."
    except Exception as e:
        return f"Erro inesperado: {e}"

resultado = somar(10, "5")
print(resultado)