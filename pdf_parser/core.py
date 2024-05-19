import pdfplumber
from typing import Union, List
from pathlib import Path


class PDFParser:
    """
    A class to parse PDF content and write it to a text file.
    """

    def __init__(self, pdf_path: Union[str, Path]):
        """
        Initialize the PDFParser with the path to the PDF file.

        Args:
            pdf_path (Union[str, Path]): The path to the PDF file to be parsed.
        """
        self.pdf_path = Path(pdf_path)

    def parse_to_file(self, parsed_file_path: Union[str, Path] = None) -> Union[str, Path]:
        """
        Parses the PDF content and writes it to a text file.

        Args:
            parsed_file_path (Union[str, Path], optional): Path to the parsed text file.
                Defaults to None, in which case the parsed file will have the same
                name as the PDF file with "_core_parsed.txt" appended.

        Returns:
            Union[str, Path]: The path to the parsed text file.

        Raises:
            FileNotFoundError: If the PDF file is not found.
        """
        try:
            # Open the PDF file using pdfplumber
            with pdfplumber.open(self.pdf_path) as pdf:
                # Extract text from each page and join with double newlines
                text = "\n\n".join([page.extract_text() for page in pdf.pages])

            # If no parsed path is given, create a default parsed file path
            if not parsed_file_path:
                parsed_file_path = self.pdf_path.with_name(f"{self.pdf_path.stem}_core_parsed.txt")

            # Write the extracted text to the parsed file
            with open(parsed_file_path, "w", encoding="utf-8") as f:
                f.write(text)

            return parsed_file_path
        except FileNotFoundError as e:
            # Raise an error if the PDF file is not found
            raise e
