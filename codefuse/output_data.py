from dataclasses import dataclass

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
            print(f"Error writing to {path}: {e}")
        else:
            print(f"Output successfully written to {path}")
            
    def to_clipboard(self) -> None:
        """
        Copies the merged content to the clipboard.
        """
        import pyperclip
        pyperclip.copy(self.merged_content)
        print("Output successfully copied to clipboard")
            
    