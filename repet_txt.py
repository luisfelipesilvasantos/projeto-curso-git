# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Solicitando uma string
string = input("Digite um palavra: ") + ""

# Solicitando um número inteiro
numero = int(input("Digite um numero inteiro : "))  # Convertemos a entrada para inteiro

print((string + ' ')* numero)