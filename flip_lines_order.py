import sys

def flip_lines():
  lines = []
  for line in sys.stdin:
      lines.append(line[:-1])  # Appends line without last character (line break)

  for line in lines[::-1]:
    print(line)

if __name__ == "__main__":
  flip_lines()
