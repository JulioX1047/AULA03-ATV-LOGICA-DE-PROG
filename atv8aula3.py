soma = 0
contador = 0

# Usamos um loop com condição baseada no contador
while contador >= 0:
    nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
    
    if nota == -1:
        break
    
    soma += nota
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
