def calcular_consumo():
    print("⚡ Calculadora de Consumo Elétrico Inteligente ⚡\n")
    
    # Coletando os dados do usuário
    nome_aparelho = input("Digite o nome do aparelho (ex: Geladeira): ")
    potencia = float(input("Digite a potência do aparelho em watts (W): "))
    horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))
    
    # Definindo o valor da tarifa (R$ 0,75 por kWh)
    tarifa_kwh = 0.75
    
    # Calculando o consumo mensal em kWh
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    
    # Calculando o custo estimado em Reais
    custo_estimado = consumo_mensal * tarifa_kwh
    
    # Exibindo os resultados formatados
    print("\n-------------------------")
    print("📊 RESULTADO DA ESTIMATIVA")
    print("-------------------------")
    print(f"Aparelho: {nome_aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo_estimado:.2f} por mês")
    print("-------------------------\n")

if __name__ == "__main__":
    calcular_consumo()