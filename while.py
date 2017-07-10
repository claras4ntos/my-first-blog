question = "Voce é brasileiro?"

possible_answers = ["Yes", "No"]

answer = None
while answer not in possible_answers:
    print(question)
    for possible_answer in possible_answers:
        print(possible_answer)

    answer = input(">>> ")


people = ["Nola", "Bianca", "Pedro"]

index = 0

while index < len(people):
    print("Hi, {}".format(people[index]))
    index = index + 1
