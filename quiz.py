questions = [
    [{
        "question": "Qual é o nome do cachorro da Amanda?",
        "possible_answers": [
            "1. Carol",
            "2. Ghost",
            "3. Fluffy",
            "4. Diamante",
        ],
        "correct_answer": '2'
    },
    {
        "question": "Qual é a cor preferida da Clara?",
        "possible_answers": [
            "1. laranja",
            "2. azul",
            "3. verde",
            "4. rouxo",
        ],
        "correct_answer": '3'
    },
    {
        "question": "Oque os guris nao gostam de fazer?",
        "possible_answers": [
            "1. fumar maconha",
            "2. escutar musica alta",
            "3. tomar refrigerante",
            "4. lavar loca",
        ],
        "correct_answer": '4'
    },
],

result = 0

for question_definition in questions:
    print(question_definition["question"])
    for possible_answer in question_definition["possible_answers"]:
        print (possible_answer)

    answer = input(">>> ")
    if answer.strip() == question_definition["correct_answer"]:
        result = result + 1

print ("Voce acertou {} de 3 questoes".format(result))
