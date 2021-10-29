def distancia(lista1, lista2) -> float:
    """
    Calcula la distancia euclídea de dos listas
    """
    cuadrados = [(p - q)**2 for p, q in zip(lista1, lista2)]
    return sum(cuadrados)**.5
