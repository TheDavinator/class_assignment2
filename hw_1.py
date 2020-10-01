# function to find class average grade score 
def calculate_averge(students):
    i = 0
    total = 0
    while i < students:
        grade = int(input("Put the score for the student here: "))
        total += grade
        i += 1
        if i == students:
            average = total / i
            return average  

students = int(input("Put the numbers of student in the class here: ")) # Used to take user input 
output = calculate_averge(students) # Used to call the calulation function
print("The average for the class is: ", output)
