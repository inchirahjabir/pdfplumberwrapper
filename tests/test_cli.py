"""
Unit tests for the PDFPlumberWrapper CLI.

These tests cover the functionality of the PDFParser class:
- Parsing a PDF to a file with the default parsed file path.
- Parsing a PDF to a file with a custom parsed file path.
- Handling non-existent PDF files.
- Handling non-PDF files.
"""

import os
import sys
import subprocess
import pytest


def test_cli_with_default_path():
    """
    Test CLI with the default parsed file path.

    The parsed file will be named based on the PDF file name with "_cli_parsed.txt" appended.
    """
    pdf_path = "tests/files/test_pdf.pdf"

    # Construct the command using the Python interpreter path
    command = f"{sys.executable} ./cli.py {pdf_path}"

    # Run the command using subprocess
    subprocess.run(command, shell=True, check=True, cwd=os.getcwd())

    # Verify the parsed file exists
    default_parsed_file_path = f"{pdf_path[:-4]}_cli_parsed.txt"
    assert os.path.isfile(default_parsed_file_path)

    # Clean up: Remove the created parsed file
    os.remove(default_parsed_file_path)


def test_cli_with_custom_path():
    """
    Test CLI with a custom parsed file path.

    The parsed file will be named based on the provided path.
    """
    pdf_path = "tests/files/test_pdf.pdf"
    custom_parsed_file_path = "tests/files/cli_custom_parsed_file.txt"

    # Construct the command using the Python interpreter path
    command = f"{sys.executable} ./cli.py {pdf_path} -o {custom_parsed_file_path}"

    # Run the command using subprocess
    subprocess.run(command, shell=True, check=True, cwd=os.getcwd())

    # Verify the parsed file exists
    assert os.path.isfile(custom_parsed_file_path)

    # Clean up: Remove the created parsed file
    os.remove(custom_parsed_file_path)


def test_cli_with_invalid_pdf():
    """
    Test CLI with a non-existent PDF file.

    This should raise a subprocess.CalledProcessError.
    """
    pdf_path = "tests/files/not_found.pdf"

    # Construct the command using the Python interpreter path
    command = f"{sys.executable} ./cli.py {pdf_path}"

    # Run the command using subprocess and expect an error to be raised
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.run(command, shell=True, check=True, cwd=os.getcwd())


def test_cli_with_non_pdf_file():
    """
    Test CLI with a non-PDF file.

    This should print an error message and not create a parsed file.
    """
    non_pdf_path = "tests/files/not_a_pdf.txt"
    parsed_file_path = "tests/files/not_a_pdf_cli_parsed.txt"

    # Construct the command using the Python interpreter path
    command = f"{sys.executable} ./cli.py {non_pdf_path} -o {parsed_file_path}"

    # Run the command using subprocess and expect it to complete without creating the parsed file
    subprocess.run(command, shell=True, check=False, cwd=os.getcwd())

    # Verify the parsed file does not exist
    assert not os.path.isfile(parsed_file_path)
