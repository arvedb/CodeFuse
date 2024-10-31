"""
CodeFuse Core Module.

This module contains the `CodeFuse` class, which is responsible for scanning
directories, filtering files based on specified templates, and combining the
content of the selected files into a single consolidated output.
"""

import os
from typing import List

from .templates import default_template, Template
from .files import File


class CodeFuse:
    """
    CodeFuse Class.

    Handles the aggregation and merging of code files from a specified directory
    based on inclusion or exclusion templates.

    Attributes:
        folder (str): Path to the target directory to process.
        template (Template): Template defining which file extensions to include or exclude.
        all_files (List[File]): List of all files found in the target directory.
        included_files (List[File]): List of files that match the inclusion criteria.
        excluded_files (List[File]): List of files that do not match the inclusion criteria.
    """

    def __init__(self, folder: str, template: Template = default_template) -> None:
        """
        Initialize the CodeFuse instance.

        Args:
            folder (str): Path to the directory to be processed.
            template (Template, optional): Template to determine file inclusion/exclusion.
                Defaults to `default_template`.
        
        Raises:
            ValueError: If the provided folder path does not exist or is not a directory.
        """
        if not os.path.isdir(folder):
            raise ValueError(f"The provided folder path '{folder}' is not a valid directory.")

        self.folder = folder
        self.template = template
        self.all_files = self._get_all_files()
        self.included_files = [
            file for file in self.all_files if self.template.does_include(file.extension)
        ]
        self.excluded_files = [
            file for file in self.all_files if not self.template.does_include(file.extension)
        ]

    def _get_all_files(self) -> List[File]:
        """
        Retrieve all files from the target directory and its subdirectories.

        Traverses the directory tree starting from `self.folder` and collects all files.

        Returns:
            List[File]: A list of `File` instances representing each file found.
        """
        all_files = []
        for root, _, files in os.walk(self.folder):
            for filename in files:
                file_path = os.path.join(root, filename)
                all_files.append(File(file_path))
        return all_files

    def _combine_files(self, files: List[File]) -> str:
        """
        Combine the contents of the specified files into a single string.

        Each file's content is separated by a line of dashes and includes the file path
        for reference.

        Args:
            files (List[File]): List of `File` instances to be combined.

        Returns:
            str: The combined content of all specified files.

        Raises:
            Exception: If there's an error reading any of the files.
        """
        if not files:
            return ""

        combined_content = []
        separator = "-" * 80  # Separator line for clarity between files

        for file in files:
            try:
                content = file.content
                combined_content.append(f"{separator}\n\n{file.path}\n\n{content}")
            except Exception as e:
                raise Exception(f"Error combining file {file.path}: {e}")

        return "\n\n".join(combined_content)

    @property
    def output(self) -> str:
        """
        Get the combined output of all included files.

        Combines the contents of `self.included_files` using the `_combine_files` method.

        Returns:
            str: The consolidated content of all included files.
        """
        return self._combine_files(self.included_files)

    def write_output(self, path: str):
        """
        Write the combined output to a specified file.

        Excludes the output file itself from being included in future aggregations to prevent
        recursive inclusion.

        Args:
            path (str): The file path where the combined output will be written.

        Raises:
            Exception: If there's an error writing to the specified file.
        """
        output_file = File(path)

        # Exclude the output file from the list of all files to prevent self-inclusion
        self.all_files = [
            file for file in self.all_files if file.name != output_file.name
        ]

        try:
            with open(path, "w", encoding="utf-8") as outfile:
                outfile.write(self.output)
        except Exception as e:
            print(f"Error writing to {path}: {e}")
