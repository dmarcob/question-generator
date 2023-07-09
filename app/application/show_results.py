from app.domain.user_interface import UserInterface
from app.domain.test import Test
from typing import List

def show_results(tests:List[Test],user_interface:UserInterface):
  user_interface.show_results(tests)
