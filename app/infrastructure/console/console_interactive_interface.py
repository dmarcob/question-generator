from app.domain.interactive_interface import InteractiveInterface

class ConsoleInteractiveInterface(InteractiveInterface):

  def get_input(self, message:str):
    return input(message + ": ")

  def show_message(self, message):
    print(message)