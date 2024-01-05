import random
class SeaAnimal:

    def __init__(self,position):
        self.x, self.y = position

class Fish(SeaAnimal):
    def __init__(self, position):
        super().__init__(position)

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

        if grid[new_x][new_y] == 0:
            grid[self.x][self.y] = 0
            self.x, self.y = new_x, new_y

        
        grid[self.x][self.y] = 'F'

        print(self.x,self.y)

class Shark(SeaAnimal):

    def __init__(self, position):
        super().__init__(position)

    def shark_move(self,grid):
        new_x, new_y = self.x, self.y
        direction = random.choice(['north', 'south', 'east', 'west'])

         
        if grid[self.x + 1][self.y] == 'F':
            new_x = self.x + 1
        elif grid[self.x - 1][self.y] == 'F':
            new_x = self.x - 1
        elif grid[self.x][self.y + 1] == 'F':
            new_y = self.y + 1
        elif grid[self.x][self.y - 1] == 'F':
            new_y = self.y - 1

        else:
            if direction == 'north':
                new_y += 1
            elif direction == 'south':
                    new_y -= 1
            elif direction == 'west':
                new_x -= 1
            elif direction == 'east':
                new_x += 1

        grid[self.x][self.y] = 0  
        if grid[new_x][new_y] == 'F':
            grid[new_x][new_y] = 'S'
        else:
            
            grid[new_x][new_y] = 'S'
            self.x, self.y = new_x, new_y
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