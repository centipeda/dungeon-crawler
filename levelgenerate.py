class Grid:
    def __init__(self,width,height):
        self.width = width
        self.length = height
        self.grid = self._init_grid()

    def _init_grid(self):
        grid = []
        for n in self.height:
            grid.append([])
        for row in grid:
            for tile in self.width:
                row.append(Tile())
        return grid

class Tile:
    def __init__(self):
        self.terrain = None
        self.item = None
        self.monster = None

class GridInteractor:
    def __init__(self):
        pass

class LevelGenerator(GridInteractor):
    def __init__(self):
        pass

class RoomGenerator(GridInteractor):
    def __init__(self):
        pass

class CorridorGenerator(GridInteractor):
    def __init__(self):
        pass

class ItemGenerator(GridInteractor):
    def __init__(self):
        pass

class MonsterGenerator(GridInteractor):
    def __init__(self):
        pass
