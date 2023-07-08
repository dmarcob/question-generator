from app.domain.user_interface import UserInterface
from app.domain.question import Question

def process_answer(question:Question, user_interface:UserInterface):
  answer = user_interface.get_input(question)
  if(answer == question.answer):
    user_interface.show_message("OK")
  else:
    user_interface.show_message("TRY AGAIN")
    process_answer(question, user_interface)
