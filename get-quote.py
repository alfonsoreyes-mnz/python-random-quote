"""
#see what is inside of folder
#linea agregada desde la consola
import os

entries = os.listdir('python-random-quote/')

print(entries)
"""
def main():
  print("Keep it logically awesome.")

  f = open("quotes.txt","r") #changed because of python doesn't find file
  quotes = f.readlines()
  f.close()

  for item in quotes:
    print(item)  #making list of lines from file


if __name__== "__main__":
  main()
