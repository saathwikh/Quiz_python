def load_questions():
  questions = {
    "What is the tallest mountain in the world?": {
      "options": ["A. Mount Everest", "B. K2", "C. Kangchenjunga", "D. Lhotse"],
      "answer": "A"
    },
    "What is the name of the world's largest ocean?": {
      "options": ["A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. Arctic Ocean"],
      "answer": "A"
    },
    "In which year did the first successful powered flight occur?": {
      "options": ["A. 1903", "B. 1899", "C. 1912", "D. 1920"],
      "answer": "A"
    }
  }
  return questions

def user_input(prompt, valid_options):
    while True:
        answer = input(prompt).strip().upper()
        if answer in valid_options:
            return answer
        else:
            print(f"Invalid option. Please enter one of the following: {', '.join(valid_options)}")

def provide_feedback(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!\n")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.\n")

def calculate_score(user_answers, correct_answers):
    """Calculate the user's score."""
    score = 0
    for question in user_answers:
        if user_answers[question] == correct_answers[question]:
            score += 1
    return score

def display_final_score(score, total_questions):
    """Display the final score."""
    print(f"Your final score is {score} out of {total_questions}.")

def main():
    """Main function to run the quiz."""
    questions = load_questions()
    correct_answers = {question: details["answer"] for question, details in questions.items()}
    user_answers = {}

    for question, details in questions.items():
        print(question)
        for option in details["options"]:
            print(option)
        user_answer =user_input("Your answer: ", [opt[0] for opt in details["options"]])
        user_answers[question] = user_answer
        provide_feedback(user_answer, details["answer"])

    score = calculate_score(user_answers, correct_answers)
    display_final_score(score, len(questions))

if __name__ == "__main__":
    main()
