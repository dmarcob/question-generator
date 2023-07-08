from app.domain.interactive_interface import InteractiveInterface

def process_answer(question:str, valid_answer:str, interactiveInterface:InteractiveInterface):
  answer = interactiveInterface.get_input(question)
  if(answer == valid_answer):
    interactiveInterface.show_message("OK")
  else:
      interactiveInterface.show_message("TRY AGAIN")
      process_answer(question, valid_answer, interactiveInterface)
