import os
from typing import List
from dataclasses import dataclass, field
from templates import Template
from files import File


@dataclass
class AppData:
    """
    AppData holds and manages file information in a given folder based on a Template.
    - 'template' controls which extensions are included or excluded.
    - 'folder' is the root directory to scan.
    - 'all_files' is populated at instantiation time.
    """
    template: Template
    folder: str
    all_files: List[File] = field(init=False)

    def __post_init__(self):
        # Gather all files in the given folder
        self.all_files = self._get_all_files()

    def _get_all_files(self) -> List[File]:
        """
        Recursively walks through 'folder' to collect all files into a list of File objects.
        """
        all_files = []
        for root, _, files in os.walk(self.folder):
            for filename in files:
                path = os.path.join(root, filename)
                all_files.append(File(path))
        return all_files

    @property
    def included_files(self) -> List[File]:
        """
        Returns all files whose extension matches the template's criteria for inclusion.
        """
        return [f for f in self.all_files if self.template.does_include(f.extension)]

    @property
    def excluded_files(self) -> List[File]:
        """
        Returns all files whose extension does NOT match the template's criteria for inclusion.
        """
        return [f for f in self.all_files if not self.template.does_include(f.extension)]

