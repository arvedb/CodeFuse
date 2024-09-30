import os
from dataclasses import dataclass, field
from templates import Template
from files import File


@dataclass
class AppData:
    template: Template
    folder: str
    output: str = field(default=None)
    output_file_path: str = field(default=None)

    all_files: list[File] = field(init=False)
    included_files: list[File] = field(init=False)
    excluded_files: list[File] = field(init=False)

    def __post_init__(self):
        self.all_files = self._get_all_files()
        self.included_files = [
            file
            for file in self.all_files
            if self.template.does_include(file.extension)
        ]
        self.excluded_files = [
            file
            for file in self.all_files
            if not self.template.does_include(file.extension)
        ]

    def _get_all_files(self) -> list[File]:
        all_files = []
        for root, _, files in os.walk(self.folder):
            for filename in files:
                all_files.append(File(os.path.join(root, filename)))
        return all_files

