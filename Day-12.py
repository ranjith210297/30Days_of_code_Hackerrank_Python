class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    
    def __init__(self,firstName, lastName, id, scores):
        super().__init__(firstName,lastName, id)
        self.scores = scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        summ = 0
        for i in scores:
            summ += i
        grade = summ/len(scores)
        if grade>=90 and grade<=100:
            grade = "O"
        elif grade >=80 and grade < 90:
            grade = "E"
        elif grade>=70 and grade<80:
            grade = "A"
        elif grade >=55 and grade < 70:
            grade = "P"
        elif grade >=40 and grade <55:
            grade = "D"
        elif grade < 40:
            grade = "T"
        
        return grade
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())