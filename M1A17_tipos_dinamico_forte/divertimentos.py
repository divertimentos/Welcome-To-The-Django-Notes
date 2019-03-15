# O Sistema de tipos: Dinâmico e Forte

letras = "abc"

letras.upper()

# O código 1 + "1" dá um erro porque a tipagem do Python é forte.

# Já o código abaixo roda:

1 + int("1")  # 2
str(1) + "1"  # "11"

# O Python não converte o "1" em inteiro, ele cria um novo objeto de tipo int()

# Sobrecarga de operadores:

# Isto são açúcares sintáticos:
"1" + str(1)  # "11"
int("1") + 1  # 2

# Que são o mesmo que:
"1".__add__(str(1))
int("1").__add__(1)

#

3 * 42  # 126
"#" * 42

# São o mesmo que:

"#".__mul__(42)
int(3).__mul__(42)

# Caso-limite:

3 % 2  # 1

int(3).__mod__(2)  # 1

"Olá, %s!" % "Kendrick"  # "Olá, Kendrick"

print("Olá, %s! %s" %("Kendrick", "Bom dia!"))

# Que é o mesmo que:
print("Olá, %s! %s".__mod__(("Kendrick", "Bom dia!")))
