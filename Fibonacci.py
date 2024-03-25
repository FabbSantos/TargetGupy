def fibonacci(n):
  """
  Função que calcula a sequência de Fibonacci até o n-ésimo termo.

  Args:
    n: Número inteiro que representa a quantidade de termos da sequência.

  Returns:
    Uma lista com os n primeiros termos da sequência de Fibonacci.
  """
  if n == 0:
    return [0]
  elif n == 1:
    return [0, 1]
  else:
    sequencia = fibonacci(n - 1)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def main():
  """
  Função principal que verifica se um número pertence à sequência de Fibonacci.

  Args:
    Nenhum.

  Returns:
    Nenhum.
  """
  # Número a ser verificado
  numero = 13

  # Cálculo da sequência de Fibonacci
  sequencia = fibonacci(numero)

  # Verificação se o número pertence à sequência
  if numero in sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
  else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
  main()
