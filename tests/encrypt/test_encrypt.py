from challenges.challenge_encrypt_message import encrypt_message
import pytest

# Requisito 2: Criptografia de inversões (Testes)
# keys
key_par = 2
key_impar = 3
key_tipo_errado = 'oi'
key_negativa = -2

# entrada
mensagem = 'isabel'
mensagem_tipo_errada = 16

# error messages
key_errada = "tipo inválido para key"
message_errada = "tipo inválido para message"


def test_encrypt_message():
    # Se key e message não possuírem os tipos corretos,
    # uma exceção deve ser lançada
    with pytest.raises(TypeError, match=key_errada):
        encrypt_message(mensagem, key_tipo_errado)
    with pytest.raises(TypeError, match=message_errada):
        encrypt_message(mensagem_tipo_errada, key_impar)

    # Se key for ímpar: divide message no índice key,
    # inverte os caracteres de cada parte, e retorna
    # a união das partes novamente com "_" entre elas
    assert encrypt_message(mensagem, key_impar) == 'asi_leb'

    # Se key for par: divide message no índice key,
    # inverte a posição das partes, inverte os caracteres
    # de cada parte, e retorna a união das partes novamente
    # com "_" entre elas
    assert encrypt_message(mensagem, key_par) == 'leba_si'

    # Se key não for um índice positivo válido de message,
    # retorna a string message invertida
    assert encrypt_message(mensagem, key_negativa) == 'lebasi'
