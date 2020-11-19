import random

participantes = []

status = True

while status:
    users = input("Insert users username or type 'draw' to exit and random select one: ")
    tam_inp = len(users)
    if tam_inp < 4:
        print("Username must have at least 4 characters! Try again.")
    else:
        participantes.append(users)
        lst_size = len(participantes)
        for i in participantes:
            print(i)
        if users == "draw":
            rnd = random.randint(-1, lst_size)
            print("Parabéns ao" + participantes[rnd] + " pela vitória!")
            status = False
