from .tile import Tile
import base64


class Chunk:
    def __init__(self, ind: list[int], version: int = 6):
        self.chunksize: int = 16

        self.ind = ind # [x, y]
        self.tiles = [[None] * self.chunksize] * self.chunksize
        self.version = version

        for y in range(self.chunksize):
            for x in range(self.chunksize):
                self.tiles[y][x] = Tile(
                        x= self.ind[0] * self.chunksize + x,
                        y= self.ind[1] * self.chunksize + y,
                        tile= "Space"
                    )


    def _serialize(self, tilemap: dict) -> dict:
        return {
                "ind": ",".join([str(i) for i in self.ind]),
                "tiles": "".join([
                    "".join([base64.b64encode(
                        tilemap[tile.name].to_bytes(2, 'big') +
                        tile.metadata.to_bytes(2, 'big') +
                        tile.variation.to_bytes(2, 'big')
                    ).decode('utf-8') for tile in row])
                for row in self.tiles]),
                "version": self.version
                }


    def setTile(tile: Tile):
        self.tiles[tile.y % self.chunksize][tile.x % self.chunksize] = tile

