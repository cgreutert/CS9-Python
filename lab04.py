from Stack import Stack
def solveMaze(maze, startX, startY):
    s = Stack()
    s.push([startX, startY])
    count = 1
    while s.isEmpty() != True:
        x = s.peek()[0]
        y = s.peek()[1]
        originalCount = count
        if maze[x][y] == 'G':
            return True
        if maze[x][y] == ' ':
            maze[x][y] = count
            count += 1
        if x > 0 and (maze[x-1][y] == 'G' or maze[x-1][y] == ' '):
            s.push((x-1,y))
            continue
        elif y > 0 and (maze[x][y-1] == 'G' or maze[x][y-1] == ' '):
            s.push((x,y-1))
            continue
        elif x < len(maze) -1  and (maze[x+1][y] == 'G' or  maze[x+1][y] == ' '):
            s.push((x+1,y))
            continue
        elif y < len(maze[x])-1  and (maze[x][y+1] == 'G' or maze[x][y+1] == ' '):
            s.push((x,y+1))
            continue
        if originalCount == count:
            s.pop()
    return False

