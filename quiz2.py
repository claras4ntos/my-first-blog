question_1 = """Qual o nome do cachorro da Amanda??
    1. Carol\n
    2. Ghost\n
    3. Fluffy\n
    4. Diamante\n"""

question_2 = """Qual é a cor preferida da Clara?
    1. laranja\n
    2. azul\n
    3. verte\n
    4. rouxo\n"""
question_3 = """Oque o Nola nao gosta de fazer?
    1. fumar maconha\n
    2. escutar musica alta\n
    3. tomar refrigerante\n
    4. lavar loca\n"""

answer_1 = input(question_1)
answer_2 = input(question_2)
answer_3 = input(question_3)

result = 0

if answer_1 == '2':
  result = result + 1

if answer_2 == '3':
  result = result + 1

if answer_3 == '4':
  result = result + 1

print("Voce coneseguiu {} de 3 pontos! Parabens!".format(result))
