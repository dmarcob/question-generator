class Test:

  def __init__(self, name):
    self.name = name
    self.valid_answers = 0
    self.total_answers = 0
    self.valid_percentage = 0

  def increase_answer(self, is_valid):
    self.total_answers += 1
    if is_valid:
      self.valid_answers += 1
    self.calculate_valid_percentage()

  def calculate_valid_percentage(self):
    if self.total_answers <= 0:
      self.valid_percentage = 0
    self.valid_percentage = int(self.valid_answers / self.total_answers * 100)
