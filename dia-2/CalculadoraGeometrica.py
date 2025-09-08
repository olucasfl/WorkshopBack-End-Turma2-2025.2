class figuraGeometrica:
    
    formaGeometrica = input("Digite a forma geométrica (retangulo, triangulo ou circulo): ").strip().lower();

    def calcularArea(formaGeometrica):
        if formaGeometrica == "circulo":
            
            raio = input("Digite o valor do raio: ");
            pi = 3.14
            area = pi * (float(raio) ** 2);
            print(f"A área do círculo é: {area:.2f}");
            return area;

        elif formaGeometrica == "retangulo":
            base = input("Digite o valor da base: ");
            altura = input("Digite o valor da altura: ");
            area = float(base) * float(altura);
            print(f"A área do retângulo é: {area:.2f}");
            return area;
        
        elif formaGeometrica == "triangulo":
            base = input("Digite o valor da base: ");
            altura = input("Digite o valor da altura: ");
            area = (float(base) * float(altura)) / 2;
            print(f"A área do triângulo é: {area:.2f}");
            return area;

        else:
            print("Forma geométrica inválida. Por favor, escolha entre retangulo, triangulo ou circulo.");

figuraGeometrica.calcularArea(figuraGeometrica.formaGeometrica);