import random
from app.domain.question import Question
from app.domain.test import Test
from app.domain.test_repository import TestRepository

def generate_question_secuencial(test:Test, respository:TestRepository) -> Question:
  num_lines = respository.num_questions(test)
  for line in range(1, num_lines + 1):
    yield respository.read_question(test, line)

def generate_question_random(test:Test, respository: TestRepository) -> Question:
  num_lines = respository.num_questions(test)
  for random_line in random.sample(range(1, num_lines + 1), num_lines):
    # generate random questions without repetitions
    yield respository.read_question(test, random_line)
