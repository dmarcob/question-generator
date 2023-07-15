import requests
from bs4 import BeautifulSoup
import translators as ts
import re


# Script to scrap english words from www.englishrevealed.co.uk and create a csv file

URL = "https://www.englishrevealed.co.uk/FCE/fce_vocabulary2/appearance_4.php"
SOUP = BeautifulSoup(requests.get(URL).content, "html.parser")

def get_english_words():

  try:
    return get_english_words_from_string()
  except IndexError:
    print("Info: English words are not sepparated by | character")

  try:
    return get_english_words_from_html_list()
  except IndexError:
    print("Info: English words are not in html list")

  return []

def get_english_words_from_string():
  # From string sepparated with |
  return SOUP.find_all("div", class_="box")[0].text.split("|")

def get_english_words_from_html_list():
  english_words = []
  for english_word in SOUP.find_all("div", id="left-box")[0].find_all("li"):
    english_words.append(english_word.text)
  return english_words

def get_english_phrases_from_html_table():
  english_phrases = []
  gap, formatted_gap = "  ", " ___ "
  for row in SOUP.find_all("table", class_="tablecolors")[0].find_all("td"):
    formated_row = row.text[3:]
    formated_row = formated_row.replace(gap, formatted_gap)
    formated_row = formated_row.replace(" .", formatted_gap + ".")
    english_phrases.append(formated_row)
  return english_phrases

def get_english_phrases_answers():
  english_phrases_answers = []
  for row in SOUP.find_all("table", class_="popup")[0].find_all("tr"):
    formated_row = row.find_all("td")[1].text
    formated_row = re.sub(r'\([^()]*\)$', '', formated_row)
    english_phrases_answers.append(formated_row)
  return english_phrases_answers
def translate_words(words, from_language, to_language):
  translated_words = []
  for word in words:
    translated_words.append(ts.translate_text(
        word.strip(), 'google',from_language,to_language))
  return translated_words

def generate_output_file(questions, answers):
  if len(questions) != len(answers):
    print("Error: La longitud de las preguntas no coincide con las respuestas")
  output = open("../tests/" + test_name + ".csv", "w")
  for index, question in enumerate(questions):
    output.write(question + ";" + answers[index] + "\n")


if __name__ == '__main__':

  # Get test name
  test_name = URL.split("/")[-1].split(".")[0]

  # Get english words
  words = get_english_words()
  if words != []:
    palabras = translate_words(words, 'en', 'es')
    generate_output_file(questions=palabras, answers=words)

  # Get english phrases
  phrases = get_english_phrases_from_html_table()
  if phrases != []:
    phrases_answers = get_english_phrases_answers()
    generate_output_file(questions=phrases, answers=phrases_answers)