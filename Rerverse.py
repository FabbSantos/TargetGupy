def inverter_string(string):
  """
  Função que inverte os caracteres de uma string.

  Args:
    string: String que será invertida.

  Returns:
    String com os caracteres invertidos.
  """
  string_invertida = ""
  for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]
  return string_invertida

def main():
  """
  Função principal que pede a string ao usuário e a inverte.

  Args:
    Nenhum.

  Returns:
    Nenhum.
  """
  # String a ser invertida
  # string = "Olá, mundo!"

  # Entrada da string pelo usuário
  string = input("Digite a string a ser invertida: ")

  # Chamada da função para inverter a string
  string_invertida = inverter_string(string)

  # Impressão da string invertida
  print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
  main()
