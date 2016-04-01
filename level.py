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
    def __init__(self):
        self.grid = None
        self.turnCount = 0

class LevelGenerator():
    def __init__(self):
        self.level = Level()

    def create_level(self,width,height):
        self.level.grid = Grid(width,height)
        rooms = RoomGenerator()
        corridors = CorridorGenerator()
        items = ItemGenerator()
        monsters = MonsterGenerator()

        rooms.generate(self.level)
        corridors.generate(self.level)
        items.generate(self.level)
        monsters.generate(self.level)
        

class RoomGenerator():
    def __init__(self):
        pass

class CorridorGenerator():
    def __init__(self):
        pass

class ItemGenerator():
    def __init__(self):
        pass

class MonsterGenerator():
    def __init__(self):
        pass
