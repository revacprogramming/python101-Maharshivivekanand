# Using Web Services
# https://www.py4e.com/lessons/servces
maggy=False
while not maggy:
    user_entry = int(input("enter a number"))
    if user_entry == chosen_number:
        print("you win")
        maggy = True
    elif user_entry < chosen_number - 20:
        print("too low")
    elif user_entry < chosen_number - 5:
        print("low")
    elif user_entry > chosen_number + 20:
        print("too high")
    else:
        print("high")
    m+=1
    if m==6 and level_of_game=="hard":
        run_loop=True
    if m==10 and level_of_game=="easy":
        run_loop=True