#Quiz version 3


print("This is a quiz that tests your knowledge of Lana del Rey")

name = input("Enter your name:")
print("Hi there", name, "Are you ready to begin?")
print("Each question will have three possible answers")
print("...............................................................................")
print(" ")

#Set the score to 0

score = 0
score= int(score)


while True:
    
#Question #1

    print("Question #1 ")
    print(" ")
    print("What is Lana del Rey's real name ?")
    print(" ")
    print("a. Elizabeth Grant")
    print("b. Samantha Laurelson")
    print("c. Emily Johnson")

    Q1answer = "A" #correct answer
    Q1response = input("Your answer: ")

    if Q1response == "A" or Q1response == "a":
          print("Correct answer ", Q1answer)
          score = score + 1

    elif Q1response != "A" or Q1response != "a":
        print("Answer is incorrect")
        score = score + 0
        print(" ")
        print("Your current score is", score, "/8")
        print(" ")
        print("...............................................................................")
        print(" ")
          
#Question #2

    print("Question #2")
    print(" ")
    print("What was Lana del Rey's 3rd album?")
    print(" ")
    print("a. Honeymoon")
    print("b. Ultraviolence")
    print("c. Tropico")

    Q2answer = "c" #correct answer
    Q2response = input("Your answer: ")

    if Q2response == "c" or Q2response == "C":
          print("Correct answer ", Q2answer)
          score = score + 1

    elif Q2response != "c" or Q2response != "C":
          print("Answer is incorrect")
          score = score + 0
    print(" ")
    print("Your current score is", score, "/8")
    print(" ")
    print("...............................................................................")
    print(" ")

#Question #3
    
    print("Question #3")
    print(" ")
    print("What movie is Young and Beautiful featured in?")
    print(" ")
    print("a. Titanic")
    print("b. The Great Gatby")
    print("c.  Wolf of Wallstreet")

    Q3answer = "b" #correct answer
    Q3response = input("Your answer: ")

    if Q3response == "b" or Q3response == "B":
          print("Correct answer ", Q3answer)
          score = score + 1

    elif Q3response != "b" or Q3response != "B":
          print("Answer is incorrect")
          score = score + 0
    print(" ")
    print("Your current score is", score, "/8")
    print(" ")
    print("...............................................................................")
    print(" ")

#Question #4

    print("Question #4")
    print(" ")
    print("Which song is not a Lana & Weeknd collaboration?")
    print(" ")
    print("a. Lust for Love")
    print("b. Groupie Love")
    print("c.  Prisoner")

    Q4answer = "b" #correct answer
    Q4response = input("Your answer: ")

    if Q4response == "b" or Q4response == "B":
          print("Correct answer ", Q4answer)
          score = score + 1

    elif Q4response != "b" or Q4response != "B":
          print("Answer is incorrect")
          score = score + 0
    print(" ")
    print("Your current score is", score, "/8")
    print(" ")
    print("...............................................................................")
    print(" ")

#Question #5
    print("Question #5")
    print(" ")
    print("What album is the song 'American' featured in?")
    print(" ")
    print("a. Born to Die: Paradise Edition")
    print("b. Ultraviolence")
    print("c.  Honeymoon")

    Q5answer = "a" #correct answer
    Q5response = input("Your answer: ")

    if Q5response == "a" or Q5response == "A":
          print("Correct answer ", Q5answer)
          score = score + 1

    elif Q5response != "a" or Q5response != "A":
          print("Answer is incorrect")
          score = score + 0
    print(" ")
    print("Your current score is", score, "/8")
    print(" ")
    print("...............................................................................")
    print(" ")
          
#Question #6

    print("Question #6 ")
    print(" ")
    print(" What year was Lana del Rey born in?")
    print(" ")
    print("a. 1983")
    print("b. 1989")
    print("c. 1985")

    Q6answer = "c" #correct answer
    Q6response = input("Your answer: ")

    if Q6response == "c" or Q6response == "C":
          print("Correct answer ", Q6answer)
          score = score + 1

    elif Q6response != "c" or Q6response != "C":
          print("Answer is incorrect")
          score = score + 0
    print(" ")
    print("Your current score is", score, "/8")
    print(" ")
    print("...............................................................................")
    print(" ")

#Question #7

    print("Question #7 ")
    print(" ")
    print("How many more songs were released on the Paradise Edition of Born to Die?")
    print(" ")
    print("a. 7")
    print("b. 10")
    print("c. 5")

    Q7answer = "a" #correct answer
    Q7response = input("Your answer: ")

    if Q7response == "a" or Q7response == "A":
          print("Correct answer ",  Q7answer)
          score = score + 1

    elif Q7response != "A" or Q7response != "a":
          print("Answer is incorrect")
          score = score + 0
    print(" ")
    print("Your current score is", score, "/8")
    print(" ")
    print("...............................................................................")
    print(" ")

#Question #8

    print("Question #8 ")
    print(" ")
    print("How many songs does Honeymoon have?")
    print(" ")
    print("a. 14")
    print("b. 17")
    print("c. 12")

    Q8answer = "a" #correct answer
    Q8response = input("Your answer: ")

    if Q8response == "a" or Q8response == "A":
          print("Correct answer ", Q8answer)
          score = score + 1

    elif Q8response != "A" or Q8response != "a":
          print("Answer is incorrect")
          score = score + 0
    print(" ")
    print("...............................................................................")
    print(" ")

#score as a percentage

    final_score = (score*100)/8
    print("Your final score was", score)
    print("You ended with the score of" , str(final_score), "percent")
    if score >= 75.0:
        print("Congratulations!")
    else:
        print("Try again")

    answer= input("Would you like to take the quiz again?")

    if answer == "Yes" or answer == "yes":
        continue
    else:
        break
        
