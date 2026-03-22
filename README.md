# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

## 🎯 Objetivo do Sistema
Este é um projeto de iniciação em tecnologia que tem como objetivo ajudar os usuários a estimarem o gasto de energia elétrica mensal de seus aparelhos domésticos. Com base em dados simples de uso, o sistema calcula tanto o consumo em kWh quanto o custo em Reais (R$).

## 💻 Tecnologias e Linguagem
O projeto foi totalmente desenvolvido em **Python**, focando em lógica de programação, entrada de dados, cálculos matemáticos e formatação de strings.

## 🧮 Fórmula Utilizada
O cálculo do consumo mensal em kWh é feito através da seguinte fórmula matemática:

$$\text{Consumo Mensal (kWh)} = \frac{\text{Potência (W)} \times \text{Horas de Uso Diário} \times 30}{1000}$$

*Nota: Para o custo estimado em Reais, multiplicamos o resultado acima por uma tarifa fixa (ex: R$ 0,75/kWh).*

## 🚀 Como executar o programa

1. Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.
2. Faça o clone ou baixe este repositório.
3. Abra o terminal na pasta do projeto (`projetos/consumo-energia`).
4. Execute o seguinte comando:

```bash
python app.py