import subprocess
import pty
import os

# https://stackoverflow.com/questions/5411780/python-run-a-daemon-sub-process-read-stdout/5413588#5413588

def test_happy_path():
  # Given command with arguments
  command = ['python', 'main.py', '--tests', os.path.dirname(__file__)]
  master, slave = pty.openpty()

  # When is executed
  process = subprocess.Popen(
      command,
      stdin=subprocess.PIPE,
      stdout=slave,
      stderr=slave
  )
  stdout = os.fdopen(master)

  # Then prompt available tests
  assert "Available tests:" in stdout.readline()
  #assert "1 questions.csv" in stdout.readline()
  #assert "1 questions.csv" in stdout.readline()

  # -- and when choose first test, then prompt questions
  process.stdin.write("1".encode())
