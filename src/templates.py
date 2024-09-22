from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Template:
    include_extensions: Optional[List[str]] = None
    exclude_extensions: Optional[List[str]] = None
    _type: str = "include"

    def __post_init__(self):
        if self.include_extensions is not None and self.exclude_extensions is not None:
            raise ValueError(
                "Template must have either include_extensions or exclude_extensions, not both."
            )
        if self.include_extensions is None and self.exclude_extensions is None:
            raise ValueError(
                "Template must have either include_extensions or exclude_extensions."
            )

    @property
    def type(self) -> str:
        if self.include_extensions:
            return "include"
        return "exclude"

    def does_include(self, file_extension: str) -> bool:
        if self.include_extensions is not None:
            return file_extension in self.include_extensions
        return file_extension not in self.exclude_extensions


# Example usage:
default_template = Template(
    include_extensions=[".py", ".md", ".txt", ".json", ".yaml", ".yml"]
)


