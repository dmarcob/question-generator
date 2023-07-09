from app.infrastructure.csv.csv_test_repository import CSVQuestionRepository
from app.infrastructure.console.console_interface import ConsoleInterface
from app.application.select_tests import select_tests
from app.application.generate_question import generate_question_random
from app.application.check_answer import check_answer
from app.application.show_results import show_results

def main():
  question_repository = CSVQuestionRepository()

  user_interface = ConsoleInterface()

  # user select tests from all available
  selected_tests = select_tests(question_repository, user_interface)
  for test in selected_tests:
    # Generate questions and show to user
    question_generator = generate_question_random(test, question_repository)
    for question in question_generator:
      # Wait user answer and check if valid
      check_answer(test, question, user_interface)

  # show results to user
  show_results(selected_tests, user_interface)

if __name__ == '__main__':
  main()
