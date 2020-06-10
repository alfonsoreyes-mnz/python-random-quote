def main():
  print("Keep it logically awesome.")

  f = open("quotes.txt","r")
  quotes = f.readlines()
  f.close()

  print(quotes)


if __name__== "__main__":
  main()
