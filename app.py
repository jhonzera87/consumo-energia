def calcular_consumo():
    print("⚡ Calculadora de Consumo Elétrico Inteligente ⚡\n")
    
    try:
        # 1. Coleta das informações do usuário
        nome_aparelho = input("Digite o nome do aparelho (ex: Geladeira): ")
        
        entrada_potencia = input("Digite a potência do aparelho em watts (W): ")
        potencia = float(entrada_potencia.replace(",", "."))
        
        entrada_horas = input("Digite o tempo médio de uso diário em horas: ")
        horas_dia = float(entrada_horas.replace(",", "."))
        
        # 2. Cálculos de Consumo
        # A fórmula é: (Potência * Horas) / 1000 para achar o valor em kWh
        consumo_diario_kwh = (potencia * horas_dia) / 1000
        
        # Considerando um mês padrão de 30 dias
        dias_no_mes = 30
        consumo_mensal_kwh = consumo_diario_kwh * dias_no_mes
        
        # 3. Cálculo Financeiro (Estimativa)
        # Valor médio da tarifa de energia (você pode alterar esse valor depois)
        preco_kwh = 0.75 
        custo_mensal = consumo_mensal_kwh * preco_kwh
        
        # 4. Exibição dos Resultados
        print("\n" + "="*35)
        print("📊 RESULTADO DO CONSUMO")
        print("="*35)
        print(f"Aparelho: {nome_aparelho}")
        print(f"Consumo Diário: {consumo_diario_kwh:.2f} kWh")
        print(f"Consumo Mensal: {consumo_mensal_kwh:.2f} kWh (em {dias_no_mes} dias)")
        print(f"Custo Estimado: R$ {custo_mensal:.2f} por mês")
        print("="*35 + "\n")

    except ValueError:
        # Caso o usuário digite letras ao invés de números
        print("\n❌ Erro: Você digitou um valor inválido. Por favor, use apenas números para potência e horas.\n")

# Esse comando garante que o código só rode se o arquivo for executado diretamente
if __name__ == "__main__":
    calcular_consumo()