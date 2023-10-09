# Desafio 49 — Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, entretanto, agora
# um laço for.
num = int(input("Informe um número: "))

print("*-" * 10)
for i in range(0,11):
    print("{0} * {1} = {2}".format(i, num, i * num))
print("*-" * 10)
