"""
File Handling Module.

This module defines the `File` dataclass, which encapsulates information and operations
related to individual files within the CodeFuse tool. It provides properties to access
a file's extension, name, and content, facilitating easy manipulation and aggregation
of file data.
"""

import os
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class File:
    """
    File Dataclass.

    Represents a single file and provides properties to access its extension, name,
    and content. This class is used by CodeFuse to manage and process files during
    the aggregation and merging process.
    """

    path: str

    @property
    def extension(self) -> str:
        """
        Get the file's extension.

        Extracts and returns the extension of the file (e.g., '.py', '.md').

        Returns:
            str: The file extension, including the leading dot. Returns an empty
                 string if the file has no extension.
        """
        return os.path.splitext(self.path)[1]

    @property
    def name(self) -> str:
        """
        Get the file's name.

        Extracts and returns the base name of the file, excluding its directory path.

        Returns:
            str: The file name with its extension (e.g., 'script.py').
        """
        return os.path.basename(self.path)

    @property
    def content(self) -> str:
        """
        Get the file's content.

        Opens the file in read mode with UTF-8 encoding and returns its entire content
        as a string.

        Returns:
            str: The full content of the file.

        Raises:
            FileNotFoundError: If the file does not exist at the specified path.
            PermissionError: If the file cannot be accessed due to permission issues.
            UnicodeDecodeError: If the file contains characters that cannot be decoded using UTF-8.
            Exception: For any other unexpected errors that occur while reading the file.
        """
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            logger.error(f"The file '{self.path}' was not found.")
            raise
        except PermissionError:
            logger.error(f"Permission denied when accessing the file '{self.path}'.")
            raise
        except UnicodeDecodeError:
            logger.error(f"Cannot decode the file '{self.path}' using UTF-8 encoding.")
            raise
        except Exception as e:
            logger.error(f"An error occurred while reading the file '{self.path}': {e}")
            raise
