from app.domain.question import Question
from app.domain.test import Test
from typing import List

class TestRepository:

  # Returns a tuple with a question and a valid answer
  def read_question(self, test:Test, line_number:int) -> Question:
    pass

  # Returns repository size
  def num_questions(self, test:Test) -> int:
    pass

  # Returns a list with al tests
  def list_all_tests(self) -> List[Test]:
    pass
