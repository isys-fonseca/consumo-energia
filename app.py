#---ENTRADA DE DADOS---
# Pedimos as informações para o usuário.
aparelho = input("Digite o nome do aparelho:")
potencia = float(input(f"Digite a potência do(a) {aparelho} em Watts (W):"))
horas_dia = float(input(f"Quantas horas por dia o(a) {aparelho} fica ligado(a)?:"))

#---PROCESSAMENTO (CÁLCULOS)---
# Calculamos o consumo de energia por mês (30 dias) e o custo estimado.
consumoMensal = (potencia * horas_dia * 30)/1000
custoEstimado = (consumoMensal * 0.75)

#---SAÍDA DE DADOS---
# Demonstramos os resultados para o usuário.
print (f"Aparelho:{aparelho}")
print (f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print (f"Custo mensal estimado (0.75/kwh):R${custoEstimado:.2f}")
