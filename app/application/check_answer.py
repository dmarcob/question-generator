import sys

from app.domain.user_interface import UserInterface
from app.domain.question import Question
from app.domain.test import Test
def check_answer(test:Test, question:Question, user_interface:UserInterface):
  answer = user_interface.get_input(question)
  test.increase_total_answers()

  # q -> terminate program
  if(answer == Question.EXIT):
    sys.exit()

  # valid -> show valid feedback
  elif(answer == question.answer):
    test.increase_valid_ansers()
    user_interface.show_valid_feedback()

  # invalid -> recursive call to process same question again
  else:
    user_interface.show_invalid_feedback()
    check_answer(test, question, user_interface)
