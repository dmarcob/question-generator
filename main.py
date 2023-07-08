from app.infrastructure.csv.csv_test_repository import CSVQuestionRepository
from app.infrastructure.console.console_interactive_interface import ConsoleInteractiveInterface
from app.infrastructure.gui.gui_interactive_interface import GUIInteractiveInterface

from app.application.generate_secuencial_question import generate_secuencial_question
from app.application.process_answer import process_answer
from config import TESTS
import sys

def main():
  questionRepository = CSVQuestionRepository()
  interactiveInterface = GUIInteractiveInterface() if  '--ui' in sys.argv else ConsoleInteractiveInterface()

  for test in TESTS:
    question_generator = generate_secuencial_question(test, questionRepository)
    for question, valid_answer in question_generator:
      process_answer(question, valid_answer, interactiveInterface)


if __name__ == '__main__':
  main()
