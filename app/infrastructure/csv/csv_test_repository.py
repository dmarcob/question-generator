from typing import Tuple
import csv
import os
from app.domain.question_repository import QuestionRepository
from app.domain.question import Question


class CSVQuestionRepository(QuestionRepository):
  __CSV_DIR = os.path.join(os.path.dirname(__file__), "tests")

  def read(self, test_name: str, line_number: int) -> Tuple[str, str]:
    path = os.path.join(self.__CSV_DIR, test_name + ".csv")
    with open(path, "r") as csv_file:
      # Get expected row
      row = self._get_row(csv_file, line_number)
      # Return question and valid answer
      return Question(text=row[0], answer=row[1])

  def size(self, test_name: str) -> int:
    path = os.path.join(self.__CSV_DIR, test_name + ".csv")
    with open(path, "r") as csv_file:
      csv_reader = csv.reader(csv_file)
      return sum(1 for _ in csv_reader)

  # ------------ Private
  def _get_row(self, csv_file, line_number):
    csv_reader = csv.reader(csv_file)
    for _ in range(line_number - 1):
      next(csv_reader)
    return next(csv_reader)
