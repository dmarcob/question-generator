from app.infrastructure.csv.csv_test_repository import CSVQuestionRepository
from app.infrastructure.console.console_interface import ConsoleInterface
from app.infrastructure.gui.gui_interface import GUIInterface

from app.application.generate_question import generate_question
from app.application.process_answer import process_answer
from config import TESTS
import sys


def main():
  question_repository = CSVQuestionRepository()

  user_interface = GUIInterface() if '--ui' in sys.argv else ConsoleInterface()

  # User will be examined with tests specified in config.py
  for test in TESTS:
    # Generate questions in certain order
    question_generator = generate_question(test, question_repository)
    for question in question_generator:
      # Wait user answer and check if valid
      process_answer(question, user_interface)


if __name__ == '__main__':
  main()
