import os
from dataclasses import dataclass


@dataclass
class File:
    path: str
    
    @property
    def extension(self) -> str:
        return os.path.splitext(self.path)[1]
    
    @property
    def name(self) -> str:
        return os.path.basename(self.path)

    @property
    def content(self) -> str:
        with open(self.path, "r", encoding="utf-8") as file:
            return file.read()
