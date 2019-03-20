"""
Faça mágica com atribuições inteligentes
"""

table = (("Henrique", "Niterói", 22.9, 43.1), 
        ("Vinícius", "Santarém", 2.4, 54.7))

for nome, *_ in table:
    print(nome, _)


# def f(t):
#     nome, *_, = t  # É um kwarg
#     print(nome, _)

# if __name__ == "__main__":
#     f(row)
