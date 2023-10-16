def cek_euy(q1, q2):
    if q1 == "animal":
        if q2 == "no":
            print("My guess is that you are thinking of a Mouse.")
            print("I would ask if i'm right, but I don't actually care.")
        elif q2 == "yes":
            print("My guess is that you are thinking of a squirrel")
            print("I would ask if i'm right, but I don't actually care.")
        else:
            print("please just answer with 'yes' or 'no'")
    elif q1 == "vegetable":  
        if q2 == "no":
            print("My guess is that you are thinking of a carrot")
            print("I would ask if i'm right, but I don't actually care.")

        elif q2 == "yes":
            print("My guess is that you are thinking of a watermelon")
            print("I would ask if i'm right, but I don't actually care.")

        else:
            print("please just answer with 'yes' or 'no' ")
    elif q1 == "mineral":  
        if q2 == "no":
            print("My guess is that you are thinking of a paperclip")
            print("I would ask if i'm right, but I don't actually care.")

        elif q2 == "yes":
            print("My guess is that you are thinking of a Camaro")
            print("I would ask if i'm right, but I don't actually care.")

        else:
            print("please just answer with 'yes' or 'no'")
    else:
        print("I dont know that object, Please Recode me !")

print("Two Questions!")
print("Think of an object, and I'll try to guess it.\n")
print()

print("Question 1). Is it animal, vegetable, or mineral?")
q1 = input("> ")

print("Question 2). Is it bigger than a breadbox?")
q2 = input("> ")

cek_euy(q1, q2)
