import os
from typing import List
from dataclasses import dataclass, field
from templates import Template
from files import File
import logging

logger = logging.getLogger(__name__)

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
        logger.debug(f"Scanning folder: {self.folder} with template: {self.template}")
        self.all_files = self._get_all_files()
        logger.info(f"Found {len(self.all_files)} files in '{self.folder}'.")

    def _get_all_files(self) -> List[File]:
        """
        Recursively walks through 'folder' to collect all files into a list of File objects.
        """
        all_files = []
        for root, _, files in os.walk(self.folder):
            for filename in files:
                path = os.path.join(root, filename)
                all_files.append(File(path))
                logger.debug(f"Discovered file: {path}")
        return all_files

    @property
    def included_files(self) -> List[File]:
        """
        Returns all files whose extension matches the template's criteria for inclusion.
        """
        included = [f for f in self.all_files if self.template.does_include(f.extension)]
        logger.debug(f"Included {len(included)} files based on template.")
        return included

    @property
    def excluded_files(self) -> List[File]:
        """
        Returns all files whose extension does NOT match the template's criteria for inclusion.
        """
        excluded = [f for f in self.all_files if not self.template.does_include(f.extension)]
        logger.debug(f"Excluded {len(excluded)} files based on template.")
        return excluded