# Requisito 4: Anagramas (Algoritmo de ordenação)
def sort_string(string):
    lenght = len(string)
    for letter1 in range(lenght - 1):
        min = letter1
        for letter2 in range(letter1, lenght):
            if string[letter2] < string[min]:
                min = letter2
        if string[letter1] > string[min]:
            med = string[letter1]
            string[letter1] = string[min]
            string[min] = med
    sort_string = "".join(string)
    return sort_string


def is_anagram(first_string, second_string):
    palavra_1_low = [letra.lower() for letra in first_string]
    palavra_2_low = [letra.lower() for letra in second_string]
# sem diferenciar maiúsculas e minúsculas

    palavra_1_sort = sort_string(palavra_1_low)
    palavra_2_sort = sort_string(palavra_2_low)

    if len(first_string) != len(second_string):
        return (palavra_1_sort, palavra_2_sort, False)
# Retorne False se as palavras passadas por parâmetro não forem anagramas

    if first_string == "" or second_string == "":
        return (palavra_1_sort, palavra_2_sort, False)
# Retorne False se alguma das palavras passadas por parâmetro
# for uma string vazia

    if palavra_1_sort != palavra_2_sort:
        return (palavra_1_sort, palavra_2_sort, False)

    return (palavra_1_sort, palavra_2_sort, True)
# Retorne True se as palavras passadas por parâmetro forem anagramas
