"""Classes and functions for describing the state of a level."""

class Grid():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.rows = self._init_grid()
        # Rows and columns start numbered at 0.

    def _init_grid(self):
        grid = []
        for n in range(self.height):
            grid.append([])
        for row in grid:
            for tile in range(self.width):
                row.append(Tile())
        return grid
    
    def get_tile(self,row,column):
        return self.rows[column][row]

    def get_row(self,row):
        return self.rows[row]

    def get_column(self,column):
        tiles = []
        for row in self.rows:
            tiles.append(row[column])
            return tiles


class Tile:
    def __init__(self):
        self.terrain = None
        self.item = None
        self.monster = None

class Level:
    def __init__(self,width,height):
        self.grid = Grid(width,height)
        self.turnCount = 0

class LevelGenerator():
    def __init__(self):
        self.level = Level()
        
    def generate_rooms(self,level):
        pass
    
    def generate_corridors(self,level):
        pass

    def generate_items(self,level):
        pass

    def generate_monsters(self,level):
        pass

    def create_level(self,width,height):
        self.generate_rooms(self.level)
        self.generate_corridors(self.level)
        self.generate_items(self.level)
        self.generate_monsters(self.level)
        
