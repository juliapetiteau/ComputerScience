#Quiz version 2


print("This is a quiz that tests your knowledge of Lana del Rey")

name = input("Enter your name:")
print("Hi there", name, "Are you ready to begin?")
print("Each question will have three possible answers")
print("...............................................................................")

#Set the score to 0

score = 0
score= int(score)


while True:
    
#Question #1

    print("What is Lana del Rey's real name ?")

    print("a. Elizabeth Grant")
    print("b. Samantha Laurelson")
    print("c. Emily Johnson")

    Q1answer = "A" #correct answer
    Q1response = input("Your answer")

    if Q1response == "A" or Q1response == "a":
          print("Correct answer", Q1answer)
          score = score + 1

    elif Q1response != "A" or Q1response != "a":
          print("Answer is incorrect")
          score = score + 0
    print("...............................................................................")

#Question #2

    print("What was Lana del Rey's 3rd album?")

    print("a. Honeymoon")
    print("b. Ultraviolence")
    print("c. Tropico")

    Q1answer = "c" #correct answer
    Q1response = input("Your answer")

    if Q1response == "c" or Q1response == "C":
          print("Correct answer", Q1answer)
          score = score + 1

    elif Q1response != "c" or Q1response != "C":
          print("Answer is incorrect")
          score = score + 0
    print("...............................................................................")

#Question #3

    print("What movie is Young and Beautiful featured in?")

    print("a. Titanic")
    print("b. The Great Gatby")
    print("c.  Wolf of Wallstreet")

    Q1answer = "b" #correct answer
    Q1response = input("Your answer")

    if Q1response == "b" or Q1response == "B":
          print("Correct answer", Q1answer)
          score = score + 1

    elif Q1response != "b" or Q1response != "B":
          print("Answer is incorrect")
          score = score + 0
    print("...............................................................................")

#Question #4

    print("Which song is not a Lana & Weeknd collaboration?")

    print("a. Lust for Love")
    print("b. Groupie Love")
    print("c.  Prisoner")

    Q1answer = "b" #correct answer
    Q1response = input("Your answer")

    if Q1response == "b" or Q1response == "B":
          print("Correct answer", Q1answer)
          score = score + 1

    elif Q1response != "b" or Q1response != "B":
          print("Answer is incorrect")
          score = score + 0
    print("...............................................................................")

#Question #5

    print("What album is the song 'American' featured in?")

    print("a. Born to Die: Paradise Edition")
    print("b. Ultraviolence")
    print("c.  Honeymoon")

    Q1answer = "a" #correct answer
    Q1response = input("Your answer")

    if Q1response == "a" or Q1response == "A":
          print("Correct answer", Q1answer)
          score = score + 1

    elif Q1response != "a" or Q1response != "A":
          print("Answer is incorrect")
          score = score + 0
    print("...............................................................................")

#Question #6

    print("What year will Lana del Rey born in?")

    print("a. 1983")
    print("b. 1989")
    print("c.  1985")

    Q1answer = "c" #correct answer
    Q1response = input("Your answer")

    if Q1response == "c" or Q1response == "C":
          print("Correct answer", Q1answer)
          score = score + 1

    elif Q1response != "c" or Q1response != "C":
          print("Answer is incorrect")
          score = score + 0
    print("...............................................................................")

#Question #7

    print("How many more songs were released on the Paradise Edition of Born to Die")

    print("a. 7")
    print("b. 10")
    print("c. 5")

    Q1answer = "a" #correct answer
    Q1response = input("Your answer")

    if Q1response == "a" or Q1response == "A":
          print("Correct answer", Q1answer)
          score = score + 1

    elif Q1response != "A" or Q1response != "a":
          print("Answer is incorrect")
          score = score + 0
    print("...............................................................................")

#Question #8

    print("How many songs does Honeymoon have?")

    print("a. 14")
    print("b. 17")
    print("c. 12")

    Q1answer = "a" #correct answer
    Q1response = input("Your answer")

    if Q1response == "a" or Q1response == "A":
          print("Correct answer", Q1answer)
          score = score + 1

    elif Q1response != "A" or Q1response != "a":
          print("Answer is incorrect")
          score = score + 0
    print("...............................................................................")



#score as a percentage

    final_score = (score*100)/8
    print("You ended with the score of" , str(final_score), "percent")

    answer= input("Would you like to take the quiz again?")

    if answer == "Yes" or answer == "yes":
        continue
    else:
        break
        
