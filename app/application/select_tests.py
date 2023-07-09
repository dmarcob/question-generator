from app.domain.user_interface import UserInterface
from app.domain.test_repository import TestRepository

def select_tests(question_repository:TestRepository,user_interface:UserInterface):
  all_tests = question_repository.list_all_tests()
  selected_tests = user_interface.select_tests(all_tests)

  # If no test was selected, then return all available tests
  return selected_tests if selected_tests else all_tests
