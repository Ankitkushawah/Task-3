import random

def play_quiz():
  """Runs the quiz application."""

  questions = [
    {
      "question": "What is 2+2?",
      "options": ["4", "6", "8", "10"],
      "answer": "4"
    },
    {
      "question": "What is the capital of France?",
      "options": ["London", "Berlin", "Paris", "Rome"],
      "answer": "Paris"
    },
    {
      "question": "How many continents in the world?",
      "options": ["Two", "Seven", "Five", "Eleven"],
      "answer": "Seven"
    },
  ]

  score = 0
  num_questions = len(questions)

  random.shuffle(questions)

  print("Welcome to the Quiz!")

  for i, question_data in enumerate(questions):
    print(f"\nQuestion {i + 1}:")
    print(question_data["question"])

    random.shuffle(question_data["options"])
    for j, option in enumerate(question_data["options"]):
      print(f"{chr(ord('A') + j)}. {option}")

    user_answer = input("Enter your answer (A, B, C, or D): ").upper()

    if user_answer == chr(ord('A') + question_data["options"].index(question_data["answer"])):
      print("Correct!")
      score += 1
    else:
      print(f"Incorrect. The correct answer is {question_data['answer']}.")

  print(f"\nYou got {score} out of {num_questions} questions correct!")
  print(f"Your final score: {score / num_questions * 100:.2f}%")

if __name__ == "__main__":
  play_quiz()