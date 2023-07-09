from typing import Tuple
import csv
import os
from typing import List
from pathlib import Path

from app.domain.test_repository import TestRepository
from app.domain.question import Question
from app.domain.test import Test


class CSVQuestionRepository(TestRepository):
  __CSV_DIR = os.path.join(os.path.dirname(__file__), "tests")

  def read_question(self, test: Test, line_number: int) -> Question:
    if(not self._valid_csv(test)):
      print("ERROR: Test is not a csv file," + test.name)
      return -1

    path = os.path.join(self.__CSV_DIR, test.name)
    with open(path, "r") as csv_file:
      # Get expected row
      row = self._get_row(csv_file, line_number)
      # Return question and valid answer
      return Question(text=row[0], answer=row[1])

  def num_questions(self, test: Test) -> int:
    if(not self._valid_csv(test)):
      print("ERROR: Test is not a csv file," + test.name)
      return -1

    path = os.path.join(self.__CSV_DIR, test.name)
    with open(path, "r") as csv_file:
      csv_reader = csv.reader(csv_file)
      return sum(1 for _ in csv_reader)

  def list_all_tests(self) -> List[Test]:
    # Get all files and subdirectories
    files = os.listdir(self.__CSV_DIR)
    tests = []
    for index, file in enumerate(files):
      absolute_path = os.path.join(self.__CSV_DIR, file)
      test = Test(name=file)
      # If is a csv file, then append to test list
      if os.path.isfile(absolute_path) and self._valid_csv(test):
        tests.append(test)
    return tests

  # ------------ Private
  def _get_row(self, csv_file, line_number):
    csv_reader = csv.reader(csv_file)
    for _ in range(line_number - 1):
      next(csv_reader)
    return next(csv_reader)

  def _valid_csv(self, test:Test) -> bool:
    extension = Path(test.name).suffix
    return extension == '.csv'
