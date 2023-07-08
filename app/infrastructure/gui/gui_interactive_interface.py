from app.domain.interactive_interface import InteractiveInterface
import PySimpleGUI as sg

class GUIInteractiveInterface(InteractiveInterface):
  sg.theme('SystemDefaultForReal')

  def get_input(self, message:str):
    # build full window
    window = sg.Window('Test', layout=[
      [sg.Text(message)],
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

