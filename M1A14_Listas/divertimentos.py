l = ["A", "B", "C"]
print(type(l))

l.append("D")
print(l)

l.sort(reverse=True)
print(l)

# o append() retorna none, mas modifica a estrutura interna da lista
print(l.append("E"))

l2 = ["A", 1, 3.14, 10j, len, [1, 2, 3]]

print(l[0])
print(l[-1])
print(l[1:])

l[:]  # retorna uma cópia da lista

m = l

print(l, m)

print(id(l), id(m))

m.append("F")
print(l, m)

def f(x):
    x.append(42)
    return x

print(f(l), l)


def g(x):
    x = x[:]
    x.append(51)
    return x

print(g(l), l)


l = [1, 2, [4, 5, 6]]

m = l[-1]

m.append(42)
