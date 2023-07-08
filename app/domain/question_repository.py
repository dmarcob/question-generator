from typing import Tuple

class QuestionRepository:

  # Returns a tuple with a question and a valid answer
  def read(self, test_name:str, line_number:int) -> Tuple[str, str]:
    pass

  # Returns repository size
  def size(self, test_name:str) -> int:
    pass
