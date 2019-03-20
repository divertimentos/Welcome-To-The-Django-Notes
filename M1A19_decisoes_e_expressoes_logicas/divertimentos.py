nome = "henrique"
vowels = "aeiou"

for c in nome:
    if c in vowels:
        print(c.upper())
    elif c == "q":
        print("@")
    else:
        print(c)


# Expressões lógicas:

True and True  # True
True and False  # False
True or True  # True
True or False  # True
False or False  # False

bool(None)  # False
bool(False)  # False
bool(0)  # False
bool("")  # False
bool(())  # False
bool([])  # False
bool({})  # False

bool(1)  # True
bool(["abc"])  # True

# O operador lógico no Python sempre retorna o último elemento avaliado:

True and "abc"  # "abc"
True and []  # []

"abc" and True  # True
[] and True  # [] --> porque lista vazia é False

1 or []  # 1
1 or indefinido  # Retorna 1 e nem dá erro, pois ele nem olha pro segundo item

indefinido = True
1 and indefinido