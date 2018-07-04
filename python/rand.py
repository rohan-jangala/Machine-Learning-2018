import math
import sys

class student():

    def __init__(self, name, gpa, rank):
        self.name = name
        self.gpa = gpa
        self.rank = rank

    def changeRank(self, rank):
        self.rank = rank

    def changeGPA(self, gpa):
        self.gpa = gpa

    def showName(self):
        print('Student Name: ' + str(self.name))

    def showGPA(self):
        print('Student GPA: ' + str(self.gpa))

    def showRank(self):
        print('Student Rank: ' + str(self.rank))

def main():

    x = sys.argv[1]
    y = sys.argv[2]
    z = sys.argv[3]

    student1 = student(x, y, z)
    student2 = student(x, y, z)

    student1.showName()
    student1.showGPA()
    student1.showRank()

    student2.showName()
    student2.showGPA()
    student2.showRank()

    if student1.gpa == student2.gpa:

        min = min(student1.rank, student2.rank)

        student1.changeRank(min)
        student2.changeRank(min)

if __name__ == '__main__':

    main()