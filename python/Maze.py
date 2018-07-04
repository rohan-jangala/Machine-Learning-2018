def main():

    maze = [['S','F','F','F'],['F','H','F','F'],['F','H','H','F'],['F','F','F','F']]

    # for i in range(len(maze)):
    #     for j in range(len(maze[i])):
    #         print(maze[i][j], end = ' ')
    #     print()

    # sep = ''
    # end = ' '

    for i in range(len(maze)):
        s = ''
        for j in range(len(maze[i])):
            s += maze[i][j] + ' '
        print s

if __name__ == '__main__':
    main()