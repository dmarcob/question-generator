from app.domain.question import Question
from app.domain.test import Test
from typing import List


class UserInterface:

  # Shows a message and returns user input
  def get_input(self, question: Question) -> str:
    pass

  def show_valid_feedback(self):
    pass

  def show_invalid_feedback(self):
    pass

  def select_tests(self, tests: List[Test]) -> List[Test]:
    pass

  def show_qualifications(self, tests: List[Test]):
    pass