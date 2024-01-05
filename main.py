import random
class SeaAnimal:

    def __init__(self,position,animal):
        self.x, self.y = position
        self.animal = animal

class Fish(SeaAnimal):
    def __init__(self, position):
        super().__init__(position,'fish')

    def fish_move (self, grid):
    
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

        
        grid[self.x][self.y] = 'fish'

        print(self.x,self.y)

class Shark(SeaAnimal):

    def __init__(self, position,):
        super().__init__(position, "shark")

    def shark_move(self, grid):
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
        if 0 <= new_x < len(grid) and 0 <= new_y <= len(grid[0]) and grid[new_x][new_y] == 'fish':
        
            # for i in range(len(fish_list)):
            #     if fish_list[i] == new_x and fish_list[i] == new_y:
            #         fish_list.pop(i)
            #     break
           
            #position initiale:
            grid[self.x][self.y] = 0
            #nouvelle position + "fish" devient "shark"
            grid[new_x][new_y] = 'shark' 
            #MAJ coordonées
            self.x, self.y = new_x, new_y

            
        else:
            #si pas de poisson:
            grid[self.x][self.y] = 0
            grid[new_x][new_y] = 'shark'

        print(self.x, self.y)



grid = [[0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

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
for tour in range(10):
        
        for i in grid:
          print(i)
        print('tour', tour)
        
        requin.shark_move(grid)
        
        for fish in fish_list:     
                fish.fish_move(grid)