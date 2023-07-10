import argparse

from app.infrastructure.csv.csv_test_repository import CSVQuestionRepository
from app.infrastructure.console.console_interface import ConsoleInterface
from app.application.select_tests import select_tests
from app.application.generate_question import generate_question_random
from app.application.check_answer import check_answer
from app.application.show_results import show_results
from app.domain.test_repository import TestRepository
from app.domain.user_interface import UserInterface

def main(user_interface: UserInterface, test_repository: TestRepository):
  # user select tests from all available
  selected_tests = select_tests(test_repository, user_interface)
  for test in selected_tests:
    # Generate questions and show to user
    question_generator = generate_question_random(test, test_repository)
    for question in question_generator:
      # Wait user answer and check if valid
      check_answer(test, question, user_interface)

  # show results to user
  show_results(selected_tests, user_interface)

if __name__ == '__main__':
  # Create ArgumentParser
  parser = argparse.ArgumentParser()

  # Agregate an argument with name
  parser.add_argument('--ui', help='Open a GUI')
  parser.add_argument('--tests', help='Path where tests are stored')

  # Analice provided arguments
  args = parser.parse_args()

  if args.ui:
      #main(GUIInterface(), CSVQuestionRepository())
      print("WARNING: GUI is not available yet, please try another option")
  else:
    main(ConsoleInterface(), CSVQuestionRepository(args.tests))

