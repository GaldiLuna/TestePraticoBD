"""
Ler 2 valores inteiros garantindo que o segundo valor lido será sempre 
maior que o primeiro valor lido. Calcule e escreva a soma dos inteiros 
existentes entre os 2 valores lidos (incluindo os valores lidos)."
"""
def ler_valores():
    while True:
        try:
            a = int(input("Digite o primeiro valor inteiro: "))
            b = int(input("Digite o segundo valor inteiro (maior que o primeiro): "))
            if b > a:
                return a, b
            else:
                print("O segundo valor deve ser maior que o primeiro. Tente novamente.")
        except ValueError:
            print("Por favor, digite apenas números inteiros.")

def calcular_soma(a, b):
    return sum(range(a, b + 1))

def main():
    a, b = ler_valores()
    resultado = calcular_soma(a, b)
    print(f"A soma dos inteiros entre {a} e {b} é: {resultado}")

if __name__ == "__main__":
    main()


"""
Usando a seguinte lista de temperatutas 
[23.6, 37.9, 25.1, 19.0, 29.8], 
escreva código que identifique e retorne:
a) Menor temperatura
b) Maior temperatura
c) Temperatura média
"""
temperaturas = [23.6, 37.9, 25.1, 19.0, 29.8]

menor_temp = min(temperaturas)
maior_temp = max(temperaturas)
media_temp = sum(temperaturas) / len(temperaturas)

print(f"Menor temperatura: {menor_temp:.1f}°C")
print(f"Maior temperatura: {maior_temp:.1f}°C")
print(f"Temperatura média: {media_temp:.1f}°C")


"""
Faça um algoritmo para ler 50 números e armazenar em uma lista, 
verificar e escrever se existem números repetidos na lista e 
em que posições se encontram.
"""
def ler_numeros():
    numeros = []
    for i in range(50):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º número: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
    return numeros

def verificar_repetidos(numeros):
    repetidos = {}
    for i, num in enumerate(numeros):
        if num in repetidos:
            repetidos[num].append(i)
        else:
            repetidos[num] = [i]
    
    repetidos = {num: pos for num, pos in repetidos.items() if len(pos) > 1}
    return repetidos

def main():
    numeros = ler_numeros()
    repetidos = verificar_repetidos(numeros)
    
    if repetidos:
        print("Números repetidos e suas posições:")
        for num, posicoes in repetidos.items():
            print(f"Número {num} encontrado nas posições: {posicoes}")
    else:
        print("Nenhum número repetido encontrado.")

if __name__ == "__main__":
    main()


"""
Escreva uma função que recebe por parâmetro a seguinte lista 
de notas escolares [73, 67,38 ,33]. A função deve percorrer 
a lista de notas, aplicando as seguintes regras e retornar as notas finais.

Regras:

●Se a diferença entre uma nota e o próximo número múltiplo de 5 
for menor que 3, arredonde a nota para o próximo múltiplo de 5

●Se a nota for menor que 38 nada acontece com a nota.

Exemplos: Se uma nota for igual a 84, seu próximo múltiplo de 5 é 85, 
logo a nota será arredondada para para 85, pois a diferença (85-84) é menor que 3.
"""
def arredondar_notas(notas):
    notas_finais = []
    for nota in notas:
        if nota >= 38:
            proximo_multiplo = (nota // 5 + 1) * 5
            if proximo_multiplo - nota < 3:
                nota = proximo_multiplo
        notas_finais.append(nota)
    return notas_finais

# Lista de notas escolares
notas = [73, 67, 38, 33]
notas_finais = arredondar_notas(notas)
print("Notas finais:", notas_finais)

