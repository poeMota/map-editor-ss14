from .grid import Grid
from src.EntitySystem import EntitySystem


class Map:
    def __init__(self, formatId: int = 6, postmapinit: bool = False):
        self.grids = {} # uid: grid
        self.format = formatId
        self.postmapinit = postmapinit

        self.tilemap = {"Space": 0} # tileName: id


    def addGrid(self, grid: Grid) -> bool:
        if grid.uid not in self.grids:
            self.grids[grid.uid] = grid
            return True
        return False


    def _serialize(self):
        _entityMan = EntitySystem()
        return {
            "meta": {
                "format": self.format,
                "postmapinit": self.postmapinit
            },
            "tilemap": {self.tilemap[tile]: tile for tile in self.tilemap}, # id: tileName
            "entities": _entityMan._serialize()
        }

