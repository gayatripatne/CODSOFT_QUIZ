questions = ("How many planets are in the solar system?:",
             "Which is the red planet?:",
             "Which is the biggest planet in the solar system?:",
             "Which is the seventh planet in the solar system?:",
             "In which galaxy does our solar system lie?:")
             
options = (("a. 7", "b. 8", "c. 9", "d. 5"),
           ("a. Mars", "b. Jupiter", "c. Uranus", "d. Earth"),
           ("a. Mars", "b. Jupiter", "c. Uranus", "d. Earth"),
           ("a. Mars", "b. Jupiter", "c. Uranus", "d. Earth"),
           ("a. Milky Way", "b. Andromeda", "c. Whirlpool", "d. Cartwheel"))

answers = ("b", "a", "b", "c", "a")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------")
    print(question)  # Print the current question
    for option in options[question_num]:
        print(option)
    guess = input("(a, b, c, d): ").lower()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1

print("-------------")
print("heyyyyy you done really wellll.... !")
print(f"Your got: {score} out of {len(questions)}")

