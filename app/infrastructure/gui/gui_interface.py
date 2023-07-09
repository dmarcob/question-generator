from app.domain.user_interface import UserInterface
import PySimpleGUI as sg
from app.domain.question import Question

class GUIInterface(UserInterface):

  # TODO: Implement all UserInterface methods
  """
  sg.theme('SystemDefaultForReal')

  def get_input(self, question:Question):
    # build full window
    window = sg.Window('Test', layout=[
      [sg.Text(question.text)],
      [sg.Text('', size=(15,1)), sg.InputText(key='-Answer-')],
      [sg.Button('send')]
    ])

    # wait for event
    event, values = window.read()
    window.close()

    # eval
    if event == sg.WIN_CLOSED:
      return None
    elif event == "send":
      value = values["-Answer-"]
      return value

  def show_valid_feedback(self):
    # build full window
    window = sg.Window('Test', layout=[
      [sg.Text("OK")],
    ])
    # wait until timeout
    window.read(timeout=900)
    window.close()

  def show_invalid_feedback(self):
    # build full window
    window = sg.Window('Test', layout=[
      [sg.Text("TRY AGAIN")],
    ])
    # wait until timeout
    window.read(timeout=900)
    window.close()
  """
