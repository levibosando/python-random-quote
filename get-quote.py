import random

def main(data):
  # print("Keep it logically awesome.")

  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()

  #print(quotes)
  a = random.choice(data)
  print(a)

if __name__== "__main__":
  with open('quotes.txt) as f:
            data = f.readlines(data)
  main(data)
