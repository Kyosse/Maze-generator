from random import randint


class Case:
    def __init__(self, N=False, O=False, S=False, E=False):
        self.nord = N
        self.ouest = O
        self.sud = S
        self.est = E

    def __str__(self):
        return


def maze_gen(width=4, height=4):
    """
    Fonctions de générateur de labyrinthe 
    Paramètres : 
        - width(int) : correspond à la largeur du labyrinthe
        - height(int) : correspond à la hauteur du labyrinthe
    Returns :
        - 
    """

    maze = []
    for i in range(height):
        maze.append([])
        for j in range(width):
            # North,South,West,East correspond au endroit ou il y a des murs
            maze[i].append({'A': {'N': True, 'S': True, 'W': True, 'E': True}})

    # Placement du début
    xStart = randint(0, height - 2)
    yStart = randint(0, width - 2)
    if xStart > 0:
        maze[xStart][0] = {'D': {'N': True, 'S': True, 'W': False, 'E': True}}
    else:
        maze[0][yStart] = {'D': {'N': False, 'S': True, 'W': True, 'E': True}}
    # Placement du début
    xStart = randint(1, height - 1)
    yStart = randint(1, width - 1)
    if xStart > 0:
        maze[xStart][width - 1] = {'F': {'N': True,
                                         'S': True, 'W': True, 'E': False}}
    else:
        maze[height - 1][yStart] = {'F': {'N': True,
                                          'S': False, 'W': True, 'E': True}}
    print(*maze, sep='\n')

    return maze_keys(maze)


def maze_keys(maze):
    """
    Fonctions pour avoir un rendu des clés du labyrinthe
    Paramètres:
        maze (list): tableau du labyrinthe avec le dictionnaire des murs 

    Returns:
        maze_keys (list): tableau des clés des dictionnaires seulement
    """
    maze_keys = []

    for i in range(0, len(maze)):
        list = maze[i]
        maze_keys.append([])
        for dict in list:
            keys = dict.keys()
            for key in keys:
                maze_keys[i].append(key)

    return maze_keys


width = 10
height = 10


print(*maze_gen(width, height), sep='\n')
