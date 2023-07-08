from app.domain.user_interface import UserInterface
from app.domain.question import Question

class ConsoleInterface(UserInterface):

  def get_input(self, question:Question):
    return input(question.text + ": ")

  def show_message(self, message):
    print(message)