from enum import Enum
from pathlib import Path

import src.yaml as yaml
from src.Config import getConfigPath


class Selectors(Enum):
    Tile = "Tile"
    Entity = "Entity"


class Frames(Enum):
    Settings="Settings"
    Image="Image"


class GlobalSettings:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GlobalSettings, cls).__new__(cls)
            cls.instance._initialized = False
        return cls.instance


    def __init__(self):
        if not self._initialized:
            self.configPath = getConfigPath()/"config.yml"
            self.image = None
            self.outPath = None
            self.outFileName = None
            self.outFileEntry = None
            self.colorsLimit = 256

            self.colorConfig = {} # color: selector

            self.readConfig()
            self._initialized = True


    def readConfig(self):
        if self.configPath.is_file():
            data = yaml.read(self.configPath)["config"]

            self.colorsLimit = data["colorsLimit"]
            self.outPath = data["outPath"]
        else:
            self.writeConfig()


    def writeConfig(self):
        yaml.write(
                self.configPath, {
                "config": {
                    "colorsLimit": self.colorsLimit,
                    "outPath": self.outPath
            }})

