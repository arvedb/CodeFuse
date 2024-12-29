"""
CodeFuse Core Module.

This module contains the `CodeFuse` class, which is responsible for scanning
directories, filtering files based on specified templates, and combining the
content of the selected files into a single consolidated output.
"""

import logging
from templates import default_template, Template
from app_data import AppData
from output_data import Output

logger = logging.getLogger(__name__)

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
        """
        logger.debug(f"Initializing CodeFuse with folder: {folder} and template: {template}")
        self.app_data = AppData(folder=folder, template=template)

    def _combine_files(self) -> str:
        """
        Combines the content of all included files into a single string,
        along with a simple delimiter (e.g., 80 dashes).

        Returns:
            str: The combined content of all specified files.
        """
        included_files = self.app_data.included_files
        if not included_files:
            logger.warning("No files matched the inclusion criteria.")
            return ""

        combined_content = []
        for file_obj in included_files:
            combined_content.append("-" * 80)         # Delimiter
            combined_content.append(file_obj.path)    # Show file path
            combined_content.append(file_obj.content) # The file's actual content
            logger.debug(f"Added content from {file_obj.path}")
        logger.info(f"Combined content from {len(included_files)} files.")
        return "\n\n".join(combined_content)

    def generate_output(self) -> Output:
        """
        Creates and returns an Output object containing the merged file contents
        and any additional metadata (e.g., how many files were merged).

        Returns:
            Output: The output object containing the merged content.
        """
        logger.debug("Generating output.")
        content = self._combine_files()
        return Output(merged_content=content)

def main():
    codefuse = CodeFuse(".")
    output = codefuse.generate_output()
    print(output.merged_content)

if __name__ == "__main__":
    main()