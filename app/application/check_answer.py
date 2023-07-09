import sys

from app.domain.user_interface import UserInterface
from app.domain.question import Question

def check_answer(question:Question, user_interface:UserInterface):
  answer = user_interface.get_input(question)

  # q -> terminate program
  if(answer == Question.EXIT):
    sys.exit()

  # valid -> show valid feedback
  elif(answer == question.answer):
    user_interface.show_valid_feedback()

  # invalid -> recursive call to process same question again
  else:
    user_interface.show_invalid_feedback()
    check_answer(question, user_interface)
