questions = {
    "How many planets are there in solar system?": "B",
    "In what arm of Milky way does our solar system placed?": "D",
    "Who discovered The Theory of Relativity?": "A",
    "When did Python discovered?": "A"
}
options = [
    ["A. 7", "B. 8", "C. 9", "D. 10"],
    ["A. IDK", "B. M31", "C. Left Arm", "D. Orion Arm"],
    ["A. Albert Einstein", "B. Max Born", "C. R.J.Oppenheimer", "D. Nikola Tesla"],
    ["A. 1991", "B. 1990", "C. 1982", "D. 1989"]
]
question_number = 1
correct_answers = 0
total_questions = len(questions)
answer_keys = ["A", "B", "C", "D"]

def start_quiz():
    display_questions()
    grade_user()


def display_questions():
    global question_number
    for question in questions:
        print(f"<---------- Question {question_number} ---------->")
        print(f"| {question}")
        for option in options[question_number - 1]:
            print(option)
        question_number += 1
        check_answer(question)

def check_answer(key):
    global correct_answers
    correct_answer = questions.get(key).capitalize()
    choice = input("> Your answer: ").capitalize()
    while not len(choice) == 1 and choice.isdigit() and not choice.capitalize() in answer_keys:
        choice = input(" > Your answer: ").capitalize()
    if choice == correct_answer:
        correct_answers += 1
        print("|->>> True <<<-|\n")
    else:
        print("|->>> False <<<-|\n")


def grade_user():
    print("\n> Your stats are in the way!")
    grade = 100 / total_questions * correct_answers
    print(f"| Total numbers of questions >> {total_questions}")
    print(f"| Your correct answers >> {correct_answers}")
    print(f"| Your grade is {grade}%")


start_quiz()
