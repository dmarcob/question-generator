from app.domain.user_interface import UserInterface
import PySimpleGUI as sg
from app.domain.question import Question

class GUIInterface(UserInterface):
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

  def show_message(self, message):
    # build full window
    window = sg.Window('Test', layout=[
      [sg.Text(message)],
    ])
    # wait until timeout
    window.read(timeout=900)
    window.close()

