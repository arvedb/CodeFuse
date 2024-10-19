# # streamlit_app.py

# import streamlit as st
# from codefuse import CodeFuse
# from templates import Template, default_template
# from files import File
# import tempfile
# import os

# # Set the title of the app
# st.title("CodeFuse GUI")
# st.write("Merge multiple code files into a single file based on selected file types.")

# # Sidebar for file upload and options
# st.sidebar.header("Upload Files")
# uploaded_files = st.sidebar.file_uploader("Choose files", accept_multiple_files=True)

# st.sidebar.header("File Type Selection")
# include_extensions = st.sidebar.text_input(
#     "Include File Extensions (comma-separated, e.g., .py,.md,.txt)",
#     value=".py,.md,.txt,.json,.yaml,.yml"
# )

# # Parse the include extensions
# if include_extensions:
#     include_exts = [ext.strip() for ext in include_extensions.split(",") if ext.strip()]
# else:
#     include_exts = default_template.include_extensions

# # Create a Template object
# template = Template(include_extensions=include_exts)

# # Button to process files
# if st.sidebar.button("Merge Files"):
#     if not uploaded_files:
#         st.error("Please upload at least one file to proceed.")
#     else:
#         # Create File objects
#         file_objects = []
#         for uploaded_file in uploaded_files:
#             # Save uploaded files to a temporary directory
#             with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp_file:
#                 tmp_file.write(uploaded_file.getbuffer())
#                 tmp_file_path = tmp_file.name
#             file_obj = File(path=uploaded_file.name)  # Using the original file name
#             # Override the content property to read from the temp file
#             def get_content(path=tmp_file_path):
#                 with open(path, "r", encoding="utf-8") as f:
#                     return f.read()
#             file_obj.content = get_content
#             file_objects.append(file_obj)
        
#         # Initialize CodeFuse with the uploaded files and selected template
#         codefuse = CodeFuse(files=file_objects, template=template)
#         combined_output = codefuse.output

#         if not combined_output:
#             st.warning("No files matched the selected file types.")
#         else:
#             # Display the combined output in a text area
#             st.subheader("Combined Output")
#             st.text_area("Output", combined_output, height=400)

#             # Button to copy to clipboard
#             st.markdown(
#                 """
#                 <div>
#                     <button onclick="copyToClipboard()" class="copy-button">Copy to Clipboard</button>
#                 </div>
#                 <script>
#                 function copyToClipboard() {
#                     const text = document.querySelector('textarea').value;
#                     navigator.clipboard.writeText(text).then(function() {
#                         alert('Copied to clipboard!');
#                     }, function(err) {
#                         alert('Could not copy text: ', err);
#                     });
#                 }
#                 </script>
#                 <style>
#                 .copy-button {
#                     background-color: #4CAF50;
#                     border: none;
#                     color: white;
#                     padding: 10px 24px;
#                     text-align: center;
#                     text-decoration: none;
#                     display: inline-block;
#                     font-size: 16px;
#                     margin: 4px 2px;
#                     cursor: pointer;
#                 }
#                 </style>
#                 """,
#                 unsafe_allow_html=True
#             )

#             # Optionally, provide a download button
#             st.download_button(
#                 label="Download Combined Output",
#                 data=combined_output,
#                 file_name="combined_output.txt",
#                 mime="text/plain"
#             )
        
#         # Clean up temporary files
#         for file_obj in file_objects:
#             os.unlink(file_obj.content.__closure__[0].cell_contents)

# import streamlit as st
# import os
# from src.codefuse import CodeFuse
# from src.files import File
# from src.templates import Template

# st.set_page_config(page_title="CodeFuse", page_icon="🔗", layout="wide")

# st.title("CodeFuse")
# st.write("Combine your code files into a single document.")

# # File or folder selection
# selection_type = st.radio("Select input type:", ("Files", "Folder"))

# if selection_type == "Files":
#     uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
#     files = [File(file.name) for file in uploaded_files]
# else:
#     folder_path = st.text_input("Enter folder path:")
#     if folder_path:
#         files = [File(os.path.join(root, file)) for root, _, files in os.walk(folder_path) for file in files]
#     else:
#         files = []

# # File type selection
# file_types = list(set(file.extension for file in files))
# selected_types = st.multiselect("Select file types to include:", file_types, default=file_types)

# # Create Template and CodeFuse instances
# template = Template(include_extensions=selected_types)
# code_fuse = CodeFuse(files, template)

# # Combine files
# if st.button("Combine Files"):
#     combined_content = code_fuse._combine_files(code_fuse.included_files())
#     st.text_area("Combined Content", combined_content, height=400)
    
#     # Add copy to clipboard button
#     if st.button("Copy to Clipboard"):
#         st.write("Content copied to clipboard!")
#         st.experimental_set_query_params(clipboard=combined_content)

# st.sidebar.markdown("## About CodeFuse")
# st.sidebar.markdown("""
# CodeFuse is a Python tool designed to automatically combine all code files from a specified folder and its subfolders into a single file. This makes it easier to consolidate codebases, analyze or review scripts, and prepare code for text-based processing or submission to large language models (LLMs).
# """)


# gui.py

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog,
    QLabel, QListWidget, QListWidgetItem, QTextEdit, QMessageBox, QHBoxLayout, QCheckBox
)
from PyQt6.QtCore import Qt

from codefuse import CodeFuse
from templates import Template, default_template

class CodeFuseGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodeFuse GUI")
        self.setGeometry(100, 100, 800, 600)

        self.selected_paths = []
        self.is_folder = False
        self.include_extensions = []

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Selection Buttons
        selection_layout = QHBoxLayout()
        self.select_files_btn = QPushButton("Select Files")
        self.select_files_btn.clicked.connect(self.select_files)
        self.select_folder_btn = QPushButton("Select Folder")
        self.select_folder_btn.clicked.connect(self.select_folder)
        selection_layout.addWidget(self.select_files_btn)
        selection_layout.addWidget(self.select_folder_btn)
        layout.addLayout(selection_layout)

        # Label to show selected path
        self.selected_label = QLabel("No files or folder selected.")
        layout.addWidget(self.selected_label)

        # File type selection (only visible when a folder is selected)
        self.file_types_label = QLabel("Select file types to include:")
        self.file_types_label.setVisible(False)
        layout.addWidget(self.file_types_label)

        self.file_types_list = QListWidget()
        self.file_types_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.file_types_list.setVisible(False)
        layout.addWidget(self.file_types_list)

        # Generate Button
        self.generate_btn = QPushButton("Generate Combined Output")
        self.generate_btn.clicked.connect(self.generate_output)
        self.generate_btn.setEnabled(False)
        layout.addWidget(self.generate_btn)

        # Output Text Box
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Copy to Clipboard Button
        self.copy_btn = QPushButton("Copy to Clipboard")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        self.copy_btn.setEnabled(False)
        layout.addWidget(self.copy_btn)

        self.setLayout(layout)

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Files")
        if files:
            self.selected_paths = files
            self.is_folder = False
            self.selected_label.setText(f"Selected Files: {', '.join(files)}")
            self.file_types_label.setVisible(False)
            self.file_types_list.setVisible(False)
            self.generate_btn.setEnabled(True)
        else:
            self.selected_paths = []
            self.selected_label.setText("No files or folder selected.")
            self.generate_btn.setEnabled(False)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.selected_paths = [folder]
            self.is_folder = True
            self.selected_label.setText(f"Selected Folder: {folder}")
            self.populate_file_types(folder)
            self.file_types_label.setVisible(True)
            self.file_types_list.setVisible(True)
            self.generate_btn.setEnabled(True)
        else:
            self.selected_paths = []
            self.selected_label.setText("No files or folder selected.")
            self.file_types_label.setVisible(False)
            self.file_types_list.setVisible(False)
            self.generate_btn.setEnabled(False)

    def populate_file_types(self, folder):
        import os
        extensions = set()
        for root, _, files in os.walk(folder):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext:
                    extensions.add(ext)
        self.file_types_list.clear()
        for ext in sorted(extensions):
            item = QListWidgetItem(ext)
            item.setSelected(True)  # Default: all selected
            self.file_types_list.addItem(item)

    def generate_output(self):
        try:
            if self.is_folder:
                folder = self.selected_paths[0]
                selected_items = self.file_types_list.selectedItems()
                if not selected_items:
                    QMessageBox.warning(self, "No File Types Selected", "Please select at least one file type to include.")
                    return
                include_extensions = [item.text() for item in selected_items]
                template = Template(include_extensions=include_extensions)
                codefuse = CodeFuse(folder=folder, template=template)
            else:
                files = self.selected_paths
                # Create a temporary folder containing selected files
                import tempfile
                import shutil

                with tempfile.TemporaryDirectory() as temp_dir:
                    for file_path in files:
                        shutil.copy(file_path, temp_dir)
                    template = default_template  # Use default or customize as needed
                    codefuse = CodeFuse(folder=temp_dir, template=template)

            combined_output = codefuse.output
            self.output_text.setPlainText(combined_output)
            self.copy_btn.setEnabled(True)
            QMessageBox.information(self, "Success", "Combined output generated successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred:\n{e}")

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_text.toPlainText())
        QMessageBox.information(self, "Copied", "Combined output copied to clipboard.")

def main():
    app = QApplication(sys.argv)
    gui = CodeFuseGUI()
    gui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
