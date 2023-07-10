import requests
from bs4 import BeautifulSoup
import translators as ts


if __name__ == '__main__':
  url = "https://www.englishrevealed.co.uk/FCE/fce_vocabulary2/environment_4.php"
  page = requests.get(url)

  soup = BeautifulSoup(page.content, "html.parser")

  # Get test name
  test_name = url.split("/")[-1].split(".")[0]

  # Get english words
  words = soup.find_all("div", class_="box")[0].text.split("|")

  # Get spanish words
  for index, word in enumerate(words):
    palabra = ts.translate_text(word.strip(),'google','en','es')
    words[index] = palabra + "," + word.strip()

  output = open("../tests/" + test_name + ".csv", "w")
  output.write("\n".join(words))