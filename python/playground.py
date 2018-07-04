class student:
    def __init__(self, gpa, rank):
        self.gpa = gpa
        self.rank = rank

    def showGPA(self):
        print('Student GPA: ' + str(self.gpa))

    def showRank(self):
        print('Student Rank: ' + str(self.rank))

if __name__ == '__main__':
    student = student(4.73331, 1)
    student.showGPA()
    student.showRank()