# Requisito 1: Número de estudantes estudando
# no mesmo horário (Algoritmo de busca)

def study_schedule(permanence_period, target_time):
    numero_estudantes = 0

    try:
        for inicio, fim in permanence_period:
            if inicio <= target_time <= fim:
                numero_estudantes += 1
    except TypeError:
        return None
    else:
        return numero_estudantes
