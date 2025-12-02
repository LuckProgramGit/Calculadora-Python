# Calculadora Básica em Python

Este projeto é uma **calculadora simples em Python**, capaz de realizar as principais operações matemáticas entre dois números.
É um ótimo exemplo para iniciantes que estão aprendendo funções, condicionais e entrada de dados no Python.

##  Funcionalidades

A calculadora permite executar:

*  **Soma**
*  **Subtração**
*  **Multiplicação**
*  **Divisão** (com tratamento de divisão por zero)
*  **Potenciação**

##  Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Baixe ou clone o repositório.
3. Execute o arquivo:

```bash
python calculadora.py
```

##  Como funciona

O programa:

1. Solicita dois números ao usuário.
2. Mostra um menu de operações disponíveis.
3. Faz o cálculo utilizando funções separadas para cada operação.
4. Exibe o resultado no final.

Exemplo das funções:

```python
def somar(num1, num2):
    return num1 + num2

def divide(num1, num2):
    return num1 / num2
```

##  Tratamento de erros

* Impede divisão por zero.
* Exibe mensagem caso a operação escolhida seja inválida.

##  Possíveis melhorias

* Criar interface gráfica (Tkinter)
* Permitir múltiplas operações sem reiniciar o programa
* Implementar histórico de cálculos
* Adicionar testes automatizados

---

 **Projeto simples, ideal para aprendizado e prática!**
