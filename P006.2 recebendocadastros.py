nomes = []
gastos = []
totaldesconto = 0
totalloja = 0

while True:
    try:
        entrada_desconto = input("Qual o desconto do dia? ").replace(",", ".")
        desconto = float(entrada_desconto)
        break
    except ValueError:
        print("Entrada inválida! Digite um número para o desconto.")

print("-" * 20)

for i in range(5):
    nome = input("Nome do cliente: ")

    while True:
        try:
            ent_valorgasto = input(f"Total gasto: ").replace(",", ".")
            valorgasto = float(ent_valorgasto)
            break
        except ValueError:
            print("Entrada inválida! Digite um número para o valor gasto.")
    nomes.append(nome)
    gastos.append(valorgasto)

print(f"{'-'*20}")  
    
for j in range(5):   
        
    if gastos[j] > 100: 
        total=gastos[j]-desconto 
        print(f"{nomes[j]} obteve desconto, totalizando {total}")
        totaldesconto +=1
        totalloja += total

    else:
        print(f"{nomes[j]} Não tem desconto!") 
        totalloja += gastos[j]

print(f"{'-'*20}") 
print(f"Total de descontos: {totaldesconto}\nTotal recebido pela loja: {totalloja}")