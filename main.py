import random
import time
import os
class SeaAnimal:

    def __init__(self,position,animal):
        self.x, self.y = position
        self.animal = animal
        """parent class for my sea animals
        """

class Fish(SeaAnimal):
    def __init__(self, position):
        super().__init__(position,'fish')

    def fish_move (self, grid):
        """_summary_

        Args:
            grid (_type_): this method has to move a fish object within my grid (step by step) 
            but he can't move if there is a fish around him
        """
    
        direction = random.choice(['north', 'south', 'east', 'west'])
        
        new_x, new_y = self.x, self.y
       
        if direction == 'north':
            new_y += 1
        elif direction == 'south':
            new_y -= 1
        elif direction == 'west':
            new_x -= 1
        elif direction == 'east':
            new_x += 1
        #limite les déplacement des nvls coordonnée au sein de la grille
        if 0 <= new_x < len(grid) and 0 <= new_y <= len(grid[0]) and grid[new_x][new_y] == 0:
            grid[self.x][self.y] = 0
            self.x, self.y = new_x, new_y

        
            grid[self.x][self.y] = 1

        print(self.x,self.y)
    
    def reproduce(self):
        pass

class Shark(SeaAnimal):

    def __init__(self, position,):
        super().__init__(position, "shark")

    def shark_move(self, grid):
        """_summary_

        Args:
            grid (_type_): this method has to move a shark within the grid but he has to check for a fish around him first
            if there is a fish, he replaces it and else, he searches for an empty area
        """
        new_x, new_y = self.x, self.y
        direction = random.choice(['north', 'south', 'east', 'west'])

        
        if direction == 'north':
            new_y += 1
        elif direction == 'south':
            new_y -= 1
        elif direction == 'west':
            new_x -= 1
        elif direction == 'east':
            new_x += 1

        # limite horizontale et verticale de ma grille pour mes nouvelles coordonnées et vérifie si case poisson adjacente
        if 0 <= new_x < len(grid) and 0 <= new_y <= len(grid[0]) and grid[new_x][new_y] == 1 :
        
            # for i in range(len(fish_list)):
            #     if fish_list[i] == new_x and fish_list[i] == new_y:
            #         fish_list.pop(i)
            #     break
           
            #position initiale:
            #grid[self.x][self.y] = 0
            #nouvelle position + "fish" devient "shark"
            grid[new_x][new_y] = 2 
            #MAJ coordonées
            self.x, self.y = new_x, new_y

            
        else:
            #si pas de poisson:
            grid[self.x][self.y] = 0
            grid[new_x][new_y] = 2

            print(self.x, self.y)

    def reproduce(self):
        pass

    def gain_energy(self):
        pass
    
    def loose_energy(self):
        pass

grid = [[  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ],
        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ],
        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ],
        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ],
        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ],
        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ],
        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ],
        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ],
        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ],
        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]]

shark_list = []
fish_list = []

#instanciation des sharks
requin = Shark((1,1))
shark_list.append(Shark((1,1)))


#instanciation des fish
fish_list.append(Fish((0,0)))
fish_list.append(Fish((0,1)))
fish_list.append(Fish((0,2)))
fish_list.append(Fish((0,3)))
fish_list.append(Fish((2,0)))
fish_list.append(Fish((5,0)))
fish_list.append(Fish((3,0)))
fish_list.append(Fish((3,4)))
fish_list.append(Fish((5,2)))
fish_list.append(Fish((6,0)))

#boucle des chrons
for tour in range(15):
            
    for i in grid:
        print(i)
    print('tour', tour)
    
    requin.shark_move(grid)
    
    for fish in fish_list:     
            fish.fish_move(grid)
    time.sleep(0.5)
    os.system('cls')