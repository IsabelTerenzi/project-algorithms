# Requisito 3: Palíndromos (Recursividade)
def is_palindrome_recursive(word, low_index, high_index):
   # Se for passado uma string vazia, retorne False
   if word == "":
      return False
   # Retorne False se a palavra passada por parâmetro
   # não for um palíndromo
   if word[low_index] != word[high_index]:
      return False
   # Retorne True se a palavra passada por parâmetro
   # for um palíndromo
   if low_index >= high_index:
      return True
   # Chama a função novamente, agora analisando o índice seguinte
   # ao menor e o anterior ao maior, e assim sucessivamente
   return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    
