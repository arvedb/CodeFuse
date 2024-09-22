from dataclasses import dataclass



@dataclass
class DefaultTemplate:
    included_files: list = [".py", ".md", ".txt", ".json", ".yaml", ".yml"]
