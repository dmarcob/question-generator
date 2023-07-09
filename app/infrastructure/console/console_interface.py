from typing import List

from app.domain.user_interface import UserInterface
from app.domain.question import Question
from app.domain.test import Test

class ConsoleInterface(UserInterface):

  def get_input(self, question:Question):
    return input(question.text + ": ")

  def show_valid_feedback(self):
    pass

  def show_invalid_feedback(self):
    print("🟥", end=" ")

  def select_tests(self, tests: List[Test]) -> List[Test]:
    print("Available tests:")
    for index, test in enumerate(tests):
      print(str(index + 1) + " " + test.name)

    indexes = input("Select options (ej. 1,2,3): ")
    selected_tests = []
    for index in indexes.split(","):
      if not index.isdigit():
        continue
      selected_tests.append(tests[int(index) - 1])
    return selected_tests

  def show_results(self, tests: List[Test]):
    print("\nTest results:")
    for test in tests:
      print(test.name + ": " + test.calculate_result())
