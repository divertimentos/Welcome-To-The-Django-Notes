d = {"nome": "Henrique", "cidade": "Niterói", "lat": 22.9, "long": 43.1}
print(d)

print(d["nome"])
d["nome"] = "Henrique Bastos"
print(d["nome"])

# checar se uma chave existe no dicionário:
print("asdf" in d)  # deve printar False

# checar se um valor existe no dicionário:
print("Niterói" in d.values())

# checar se existe sem dar erro:
print(d.get("asdf"))

# checar se existe sem dar erro, com retorno opcional:
print(d.get("asdf", "Valor Padrão"))

# dicionary views:
k = d.keys()
v = d.values()
i = d.items()

# se você mexer no dicionário, os dicionary views vão sofrer efeito:
d["Olá"] = "Mundo!"

# deletando:
del d["Olá"]
print(d)

# adicionando:
d.update(interesses = ["Autonomia", "Hack"])
print(d)

# adicionando:
d["interesses"].append("cerveja")
print(d)

# removendo e retornando:
print(d.pop("interesses"))