from app.domain.question_repository import QuestionRepository

def generate_secuencial_question(test_name:str, respository: QuestionRepository):
  num_lines = respository.size(test_name)
  for line in range(1, num_lines + 1):
    yield respository.read(test_name, line)
