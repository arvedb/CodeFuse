from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class Output:
    """
    Holds the final merged content and any relevant metadata about the output.
    """
    merged_content: str

    def to_file(self, path: str) -> None:
        """
        Writes the merged content to the specified file path.
        """
        try:
            with open(path, "w", encoding="utf-8") as outfile:
                outfile.write(self.merged_content)
        except Exception as e:
            logger.error(f"Error writing to {path}: {e}")
        else:
            logger.info(f"Output successfully written to {path}")

    def to_clipboard(self) -> None:
        """
        Copies the merged content to the clipboard.
        """
        try:
            import pyperclip
            pyperclip.copy(self.merged_content)
        except Exception as e:
            logger.error(f"Failed to copy to clipboard: {e}")
        else:
            logger.info("Output successfully copied to clipboard")