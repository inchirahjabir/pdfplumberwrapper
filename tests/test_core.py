import pytest
import os
from pdf_parser.core import PDFParser
from pathlib import Path

def test_parse_to_file_default_path():
    """
    Test parsing a PDF to a file with the default parsed file path.
    
    The parsed file will be named based on the PDF file name with "_core_parsed.txt" appended.
    """
    # Test with a valid PDF
    pdf_path = Path("tests/files/test_pdf.pdf")
    parser = PDFParser(pdf_path)
    parsed_file_path = parser.parse_to_file()
    
    # Verify the parsed file exists
    assert Path(parsed_file_path).is_file()

def test_parse_to_file_custom_path():
    """
    Test parsing a PDF to a file with a custom parsed file path.

    The parsed file will be named based on the provided path.
    """
    # Test with a valid PDF
    pdf_path = Path("tests/files/test_pdf.pdf")
    parser = PDFParser(pdf_path)
    parsed_file_path = "tests/files/core_custom_parsed_file.txt"
    parser.parse_to_file(parsed_file_path)
    
    # Verify the parsed file exists
    assert Path(parsed_file_path).is_file()

def test_parse_to_file_path_not_found():
    """
    Test handling of a non-existent PDF file.
    
    This should raise a FileNotFoundError.
    """
    # Define a non-existent PDF path
    pdf_path = Path("tests/files/not_found.pdf")
    parser = PDFParser(pdf_path)
    
    # Expect a FileNotFoundError to be raised
    with pytest.raises(FileNotFoundError):
        parser.parse_to_file()
