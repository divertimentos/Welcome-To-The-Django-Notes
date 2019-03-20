nome = "Henrique"
print(nome, len(nome))
i = 0

while i < len(nome):
    print(nome[i])
    i += 1

for i in range(len(nome)):
    print(nome[i])

print(range(8))
r = range(8)
print(r[0])
print(r[-1])

# Saber todos os elementos do intervalo do range():
print(list(r))

# O range tem um comportamento idêntico ao dos slices

print(list(range(1, 20, 3 )))

for i in range(8):
    print(i)

# Melhorando o print da variável 'nome':
for c in nome:
    print(c)

# Iterar pelo índice:

for i, c in enumerate(nome):
    print(i, c)

# Como o enumerate() funciona:
e = enumerate("Henrique")
print(next(e))
print(next(e))

# Se você quiser, por exemplo, ignorar a letra "e":

for i, c in enumerate(nome):
    if c == "e":
        continue
    if c == "u":
        break
    print(i, c)