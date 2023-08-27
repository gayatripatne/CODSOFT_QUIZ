
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def run_quiz(self):
        score = 0
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.prompt}")
            for j, option in enumerate(question.options, 1):
                print(f"{j}. {option}")
            
            user_answer = input("Your answer (enter the option number): ")
            try:
                user_answer_index = int(user_answer) - 1
                if 0 <= user_answer_index < len(question.options):
                    if question.options[user_answer_index] == question.answer:
                        print("Correct!\n")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is {question.answer}.\n")
                else:
                    print("Invalid option number. Skipping this question.\n")
            except ValueError:
                print("Invalid input. Skipping this question.\n")

        print(f"Quiz completed. Your score: {score}/{len(self.questions)}")

# Create quiz questions
question1 = Question("What is the capital of France?",
                    ["Paris", "Berlin", "Madrid", "Rome"],
                    "Paris")

question2 = Question("Which planet is known as the 'Red Planet'?",
                    ["Mars", "Venus", "Jupiter", "Saturn"],
                    "Mars")

# Create a quiz and add questions
quiz = Quiz()
quiz.add_question(question1)
quiz.add_question(question2)

# Run the quiz
quiz.run_quiz()
