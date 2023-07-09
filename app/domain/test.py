class Test:

  def __init__(self, name):
    self.name = name
    self.valid_answers = 0
    self.total_answers = 0

  def increase_total_answers(self):
    self.total_answers += 1

  def increase_valid_ansers(self):
    self.valid_answers += 1

  def calculate_result(self):
    valid = str(self.valid_answers) + " / " + str(self.total_answers)
    percentage = self.valid_answers / self.total_answers * 100 if self.total_answers > 0 else 0
    return valid + " -> " + str(int(percentage)) + "% de aciertos"