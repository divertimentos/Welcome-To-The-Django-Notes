print(("A,", "B", "C"))

t = ("A,", "B", "C")

print(t + ("D", "E"))

print(tuple("Guilherme"))
print(tuple([1, 2, 3]))

# Tuplas aceitam  qualquer tipo de objeto:
qualquer_tipo = ("A", 1, 3.14, (2j, len), [1, 2, 3])
print(f"Qualquer tipo: {qualquer_tipo}")

print(t[0], t[1], t[2])
print(t[1:])

u = t[:]
print(id(t), id(u))

"""
Não são os parênteses que constróem a tupla. 
Quem constrói a tupla é a vírgula
"""

tupla_sem_parêntese = "C", "D", "E"
print(tupla_sem_parêntese)

print(tuple(()))