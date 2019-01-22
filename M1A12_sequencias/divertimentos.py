nome = "henrique"
print(len(nome))
print(nome[0])
print(nome[1])
# print(nome[8]) // vai dar index out of range
print(nome[-1])

# Slices
print(nome[1:7])  # "enriqu"
print(nome[1:-1])  # "enriqu"

# print(nome[1:(len(nome))])
print(nome[1:])

# Passo (slice)

print(nome[1:7:2])
print(nome[::1])
print(nome[::-1])

# Debaixo do capô:

print(nome.__len__())

print(nome.__getitem__(0))