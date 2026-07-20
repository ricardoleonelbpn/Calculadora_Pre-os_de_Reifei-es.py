"""
Objetivo: Implementar um programa que solicita ao usuário uma série
de palavras e então exibe a história com as palavras do usuário inseridas nos 
lugares apropriados.
"""
# Adicionei palavras extras para deixar a história mais personalizada e divertida
print("Por favor insira o seguinte: ")

animal = input("\nDigite um nome de um animal: ")
adjetivo1 = input("Digite um adjetivo (ex: engraçado, bonito, feio): ")
verbo1 = input("Digite um verbo (ex: correr, pular, dançar): ")
exclamacao = input("Digite uma exclamação (ex: uau!, nossa!, eita!): ").capitalize()
verbo2 = input("Digite outro verbo: ")
verbo3 = input("Digite mais um verbo: ")
verbo4 = input("Digite mais um verbo, por favor: ")
adjetivo2 = input("Digite outro adjetivo, para finalizar: ")

print("\nSua história é:")

print(f"""\nOutro dia, eu estava realmente em apuros. Tudo começou quando eu vi um {animal} {adjetivo1} {verbo1} pelo corredor. 
Eu gritei "{exclamacao}". Mas tudo que eu conseguia pensar em fazer era {verbo2} repetidamente.
Milagrosamente, isso fez com que ele parasse, mas não antes de tentar {verbo3} bem na frente da minha família.
Todos começaram a {verbo4} de mim, foi muito {adjetivo2}.""")

print()

