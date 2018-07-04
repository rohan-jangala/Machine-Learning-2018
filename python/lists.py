def main():

    supercars = ['Lamborghini', 'Ferrari', 'Bentley', 'McLaren']
    #print supercars

    # # print supercars[1]
    #
    # supercars.append('Aston Martin')
    #
    # # print supercars
    #
    # # print(len(supercars))
    #
    # supercars.pop(1)
    #
    # # print supercars
    #
    # supercars.insert(1, 'Ferrari')
    #
    # # print supercars

    # for i in range(len(supercars)):
    #     print(supercars[i])
    #
    # for i in supercars:
    #     print(i)

    points = [[2,4],[2,3],[5,5]]

    print points

    for i in points:
        for j in points[i]:
            print j

if __name__ == '__main__':
    main()