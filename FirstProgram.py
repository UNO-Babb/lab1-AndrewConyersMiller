#FirstProgram.py
#Name:Andrew Miller
#Date:8/27/24
#Assignment:Lab 1

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name
  name = input("What is your name?: ")
  print("Hello", name, "how are you?")
  #Use the user's name in the program.

  #Ask the user for their age.
  age = input("Enter your age: ")
  age = int(age)
  born = 2024 - age
  #Tell the user what year they were born in.
  print ("You were born in", born)
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
