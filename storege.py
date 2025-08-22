# No python podemos armazenar varios valores em apenas uma variével, que neste caso, elas podem ser: list, tupla, dict, set. Algumas são mutáveis, outras são imutáveis

# LISTA: as listas são geralmente usadas. São  ideias para armazenar uma coleção que pode mudar ao longo do tempo, pois são mutáveis. Ou seja, podemos alterar os valores posteriormente

# criando lista
frutas = ["laranja", "banana", "maçã"]

# adicionando um elemento
frutas.append("abacate")

# Iterando sobre frutas
for index, fruta in enumerate(frutas, start=1):
    print(f"As frutas são {index}: {fruta}")