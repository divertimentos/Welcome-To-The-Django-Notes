# M1A21: Não subestime as funções

# o def do Python apenas cria a função. Ele só a roda quando você a chama
def f():
    return 42

# Toda função em Python retorna algo. 
# Se você não explicitar nada, ela retorna None
def g():
    pass

# Parâmetro default:
def h(a, b, c="Default C"):
    print(a, b, c)

# Parâmetros posicionais indefinidos (*args):
def k(a, b, c="dC", *args):
    print(a, b, c, args)

# Parâmetros posicionais nomeados (**kwargs):
def l(a, b, c="**kwargs", **kwargs):
    print(a, b, c, kwargs)

# É possível misturar *args e **kwargs:
def m(a, b, c="dC", *args, **kwargs):
    print(a, b, c, args, kwargs)

# Keyword-only argument:
def n(a, b, c="dC", *args, x, y, **kwargs):
    print(a, b, c, x, y, args, kwargs)

# Simulando a função filter() do Django:

def filter(**lookups):
    for k, v in lookups.items():
        print(k.split('__'), v)

# Função que simplesmente recebe *args e **kwargs:
def o(*args, **kwargs):
    print(args, kwargs)

t = "A", "B", "C"
d = dict(z="Z", w="W")

# Filter():
filter(name__startswith="Hen", age__lt=30, 
        city__endswith='rói')

# Último experimento:
def add(a, b):
    return a + b

# Brincando com o dis (disassembly):
import dis

print(dis.dis(add))

# DOCSTRINGS:
def add_two(a, b):
    'Documentação da função: Soma a com b'
    return a + b


# Outro exemplo sobre como ter funções como objetos:
def calc(op, a, b):
    return op(a, b)

def mul(a, b):
    return a * b

##############################
### CHAMAMENTOS DE FUNÇÕES ###
##############################

# O def do Python apenas cria a função; o chamamento printa-a:
print(f())

# Retornando None se você não passa nada pra função:
print(g())

# Sobescrevendo parâmetro default:
print(h("A", "B", "C"))

# Parâmetros nomeados:
print(h(a="Á", b="Bê"))

# *args:
# O args é uma tupla que recebe os argumentos posicionais sem referente
print(k("A", "B", "C", "D", "E", "F"))

# Para passar quantidades ilimitadas de parâmetros nomeados, use **kwargs:
print(l(c="C", z="Z", a="A", f="F", b="B"))

# Misturando *args e **kwargs:
print(m("A", "B", "C", "D", "E", z="Z", w="W"))

# Keywork-only:
print(n("A", "B", "C", "D", "E", z="Z", x=1, y=2, w="W"))

# Função genérica, que recebe qualquer coisa:
print(o(*t, **d))
print(f"Tê e dê: {t, d}")

# Prints do último experimento (add):
print(add)
print(type(add))
print(add.__code__)
print(add.__code__.co_argcount)
print(add.__code__.co_code)
print(add.__code__.co_name)
print(add.__code__.co_varnames)

# Prints do DOCSTRINGS (add_two):
print(add_two)
print(add_two.__doc__)

# print(f"Chama o HELP: {help(add_two)}")


# Funções como objetos:
print(f"Funções como objetos: {calc(add, 2, 3)}")

print(f"Funções como objetos II: {calc(mul, 2, 3)}")
