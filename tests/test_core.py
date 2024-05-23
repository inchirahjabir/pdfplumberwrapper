"""
Unit tests for the PDFParser class.

These tests cover the functionality of the PDFParser class:
- Parsing a PDF to a file with the default parsed file path.
- Parsing a PDF to a file with a custom parsed file path.
- Handling non-existent PDF files.
- Handling non-PDF files.
"""

from pathlib import Path
import os
import pytest
from pdf_parser.core import PDFParser


def test_parse_to_file_default_path():
    """
    Test parsing a PDF to a file with the default parsed file path.

    The parsed file will be named based on the PDF file name with "_core_parsed.txt" appended.
    """
    # Test with a valid PDF
    pdf_path = Path("tests/files/test_pdf.pdf")
    parser = PDFParser(pdf_path)
    parser.parse_to_file()

    # Verify the parsed file exists
    default_parsed_file_path = pdf_path.with_name(f"{pdf_path.stem}_core_parsed.txt")
    assert default_parsed_file_path.is_file()

    # Clean up: Remove the created parsed file
    os.remove(default_parsed_file_path)


def test_parse_to_file_custom_path():
    """
    Test parsing a PDF to a file with a custom parsed file path.

    The parsed file will be named based on the provided path.
    """
    # Test with a valid PDF
    pdf_path = Path("tests/files/test_pdf.pdf")
    parser = PDFParser(pdf_path)
    parsed_file_path = Path("tests/files/core_custom_parsed_file.txt")
    parser.parse_to_file(parsed_file_path)

    # Verify the parsed file exists
    assert parsed_file_path.is_file()

    # Clean up: Remove the created parsed file
    os.remove(parsed_file_path)


def test_parse_to_file_path_not_found():
    """
    Test handling of a non-existent PDF file.

    This should raise a FileNotFoundError.
    """
    # Define a non-existent PDF path
    pdf_path = Path("tests/files/not_found.pdf")

    # Expect a FileNotFoundError to be raised
    with pytest.raises(FileNotFoundError):
        parser = PDFParser(pdf_path)
        parser.parse_to_file()


def test_non_pdf_file():
    """
    Test handling of a non-PDF file.

    This should raise a ValueError.
    """
    # Define a non-PDF file path
    non_pdf_path = Path("tests/files/not_a_pdf.txt")

    # Expect a ValueError to be raised
    with pytest.raises(ValueError):
        PDFParser(non_pdf_path)
