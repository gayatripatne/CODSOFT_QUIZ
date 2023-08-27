class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def ask_question(self):
        print(self.question)
        for index, option in enumerate(self.options):
            print(f"{index + 1}. {option}")
        
        user_choice = int(input("Enter your answer "))
        return user_choice == self.correct_option


def main():
    question1 = Question("Who is the first prime minister of india?", ["Jawaharlal Nehru", "Indira Gandhi", "Narendra Modi","Mahatma Gandhi"], Jawaharlal Nehru)
    question2 = Question("India got independence in which year?", ["1956", "1946", "1947", "2000"], 1947)
    question3 = Question("Who is also known as Shaheed-e-Azam?" , ["Bhagat Singh", "Rajguru", "Sukhdev", "Netaji Bose"], Bhagat Singh)
    question4 = Question("Codeword use by  captain vikram batra is  ",["dil to hai","dil mange more","bharat mata ki jay","vande mataram"], dil mange more)
    questions = [question1, question2, question3,question4]
    
    score = 0
    for question in questions:
        if question.ask_question():
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")
    
    print(f"Your  {score} is {len(questions)} questions correct!")

if __name__ == "__main__":
    main()