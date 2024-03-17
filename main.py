
userName = input("What is your name? ")#Ask the user to enter ther name and assign the value the variable userName
print("Hello, " + userName + "!")#Welcome the user in a print statment that displays the users name along with Hello and an exclamation point. 
print("Welcome to the Test Grader!")#print statment tells the user about the program
grade = float(input("Please enter your grade between 1 and 100: "))#Ask the user to input their grade and assign the value to the variable grade. It is a float
fail = ""#create a variable called fail that is a string
if grade > 100 or grade < 0:#if the grade is greater than 100 or less than 0 then the conditional inside will run 
  print("Invalid grade input.")#print statment tells the user that their input is invalid because the grade is greater than 100 or less than 0


if grade >= 80 and grade <= 100:#if the grade is greater than or equal to 80 and less than or equal to 100 then the conditional inside will run
  print("You got an A!")#print statment tells the user that they got an A
  fail = "N"#fail is assigned the value of N
elif grade <= 79 and grade >= 69:#if the grade is less than or equal to 79 and greater than or equal to 69 then the conditional inside
  print("You got a B!")#print statment tells the user that they got a B
  fail = "N"#fail is assigned the value of N
elif grade >= 40 and grade <= 59:#if the grade is greater than or equal to 40 and less than or equal to 59 then the conditional inside will
  print("You got a C!")#print statment tells the user that they got a C
  fail = "N"#fail is assigned the value of N
elif grade < 40 and grade >= 0:#if the grade is less than 40 and greater than or equal to 0 then the conditional inside will
  print("You got a U!")#print statment tells the user that they got a U
  fail = "Y"#fail is assigned the value of Y

if fail == "Y":#if fail is equal to Y then the conditional inside will run
  print("Retake required.")#print statment tells the user that they need to retake the test

if fail == "N":#if fail is equal to N then the conditional inside will run
  print("You passed!")#print statment tells the user that they passed the test