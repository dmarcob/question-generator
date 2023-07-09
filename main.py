from app.infrastructure.csv.csv_test_repository import CSVQuestionRepository
from app.infrastructure.console.console_interface import ConsoleInterface
from app.application.select_tests import select_tests
from app.application.generate_question import generate_question_random
from app.application.check_answer import check_answer


def main():
  question_repository = CSVQuestionRepository()

  user_interface = ConsoleInterface()

  # User will be examined with tests specified in config.py
  selected_tests = select_tests(question_repository, user_interface)
  for test in selected_tests:
    # Generate questions in certain order
    question_generator = generate_question_random(test, question_repository)
    for question in question_generator:
      # Wait user answer and check if valid
      check_answer(question, user_interface)


if __name__ == '__main__':
  main()
