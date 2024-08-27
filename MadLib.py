#MadLib.py
#Name:Andrew Miller
#Date:8/27/24
#Assignment: Lab 1 

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  noun2 = input("Enter a noun: ")
  adjective1 = input("Enter an adjective: ")
  adjective2 = input("Enter an adjective: ")
  adverb = input("Enter an adverb: ")
  #Print the story with the user supplied words.
  print("Once upon a time, there was a", adjective1, noun1, "who lived in a", adjective2, "house. Every day, the", noun1, "would", adverb, "visit the", noun2, "who lived next door. Together, they went on many", adjective2, "together.")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
