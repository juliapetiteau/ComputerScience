#Quiz !!

print("This is a quiz that tests your knowledge of Black Mirror")

name = input("Enter your name:")
print("Hi there", name, "Are you ready to begin?")
print("Each question will have three possible answers")
print("...............................................................................")

#Set the score to 0

score = 0
score= int(score)

#Question #1

print("What is the name of Episode 4 of Season 2?")

print("a. Arkangel")
print("b. White Bear")
print("c. White Christmas")

Q1answer = "C" #correct answer
Q1response = input("Your answer")

if Q1response == "c" or Q1response == "C":
      print("Correct answer", Q1answer)
      score = score + 1

elif Q1response != "C" or Q1response != "c":
      print("Answer is incorrect")
      score = score + 0
print("...............................................................................")

#Question #2

print("What is Cooper's biggest fear in Episode 2 of Seaon 3?")

print("a. Dementia")
print("b. Stroke")
print("c. Cancer")

Q1answer = "a" #correct answer
Q1response = input("Your answer")

if Q1response == "a" or Q1response == "A":
      print("Correct answer", Q1answer)
      score = score + 1

elif Q1response != "A" or Q1response != "a":
      print("Answer is incorrect")
      score = score + 0
print("...............................................................................")

#Question #3

print("What does Daly hold as leverage over Walton in 'USS Callister'?")

print("a. a toy")
print("b. a sock")
print("c.  a lollipop")

Q1answer = "C" #correct answer
Q1response = input("Your answer")

if Q1response == "c" or Q1response == "C":
      print("Correct answer", Q1answer)
      score = score + 1

elif Q1response != "C" or Q1response != "c":
      print("Answer is incorrect")
      score = score + 0
print("...............................................................................")

#score as a percentage

final_score = (score*100)/3
print("You ended with the score of" , str(final_score), "percent")
