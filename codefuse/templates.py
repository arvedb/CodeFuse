"""
Templates Module.

This module defines the `Template` dataclass, which encapsulates the criteria for
including or excluding files based on their extensions. Templates are used by the
CodeFuse tool to determine which files should be aggregated and merged. This module
also provides a default template instance for immediate use.
"""

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Template:
    """
    Template Dataclass.

    Represents a set of criteria for including or excluding files based on their extensions.
    A `Template` can either specify a list of extensions to include or a list of extensions
    to exclude. It enforces that only one of these lists is provided to avoid conflicting
    rules.

    Attributes:
        include_extensions (Optional[List[str]]): List of file extensions to include. If provided,
            only files with these extensions will be considered for aggregation.
        exclude_extensions (Optional[List[str]]): List of file extensions to exclude. If provided,
            files with these extensions will be ignored during aggregation.
        _type (str): Internal attribute indicating the type of template ('include' or 'exclude').
            Defaults to "include".
    """

    include_extensions: Optional[List[str]] = None
    exclude_extensions: Optional[List[str]] = None
    _type: str = "include"

    def __post_init__(self):
        """
        Post-initialization processing for the Template dataclass.

        Validates that the template has either `include_extensions` or `exclude_extensions`,
        but not both or neither. Raises a `ValueError` if the validation fails.

        Raises:
            ValueError: If both `include_extensions` and `exclude_extensions` are provided,
                        or if neither is provided.
        """
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
        """
        Get the type of the template.

        Determines whether the template is an inclusion or exclusion template based on
        which list of extensions is provided.

        Returns:
            str: The type of the template, either "include" or "exclude".
        """
        if self.include_extensions:
            return "include"
        return "exclude"

    def does_include(self, file_extension: str) -> bool:
        """
        Determine if a file with the given extension should be included based on the template.

        Args:
            file_extension (str): The extension of the file to check (e.g., ".py", ".md").

        Returns:
            bool: `True` if the file should be included, `False` otherwise.
        """
        if self.include_extensions is not None:
            return file_extension in self.include_extensions
        return file_extension not in self.exclude_extensions


# Example usage:
default_template = Template(
    include_extensions=[".py", ".md", ".txt", ".json", ".yaml", ".yml"]
)
