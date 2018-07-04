def main():
	print('hello world!')
	math = 27 % 6
	print(math)
	math = float(27)/6
	print(math)

def student(gpa, rank):
	gpa = gpa
	rank = rank
	print('Student GPA: ' + str(gpa))
	print('Student Rank: ' + str(rank))

if __name__ == '__main__':
	main()
	student(4.5, 1)
