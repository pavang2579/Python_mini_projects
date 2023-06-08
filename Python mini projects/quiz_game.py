print ("Welcome to the computer quiz game")

playing  =  input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! lets play :)")
score = 0

answer = input("Wnat does CPU stand for? ")
if answer.lower() == "central process unit" :
    print("correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Wnat does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Wnat does RAM stand for? ")
if answer.lower() == " Random acces memory" :
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
print("You got " + str((score/4)*100) + "%")

