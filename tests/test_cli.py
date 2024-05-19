import pytest
import subprocess
import sys
import os


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


def test_cli_with_custom_path():
    """
    Test CLI with a custom parsed file path.
    
    The parsed file will be named based on the provided path.
    """
    pdf_path = "tests/files/test_pdf.pdf"

    # Construct the command using the Python interpreter path
    command = f"{sys.executable} ./cli.py {pdf_path} -o tests/files/cli_custom_parsed_file.txt"

    # Run the command using subprocess
    subprocess.run(command, shell=True, check=True, cwd=os.getcwd())


def test_cli_with_invalid_pdf():
    """
    Test CLI with a non-existent PDF file.

    This should raise a subprocess.CalledProcessError.
    """
    pdf_path = "tests/files/not_found.pdf"

    # Construct the command using the Python interpreter path
    command = f"{sys.executable} ./cli.py {pdf_path} -o not_found.txt"

    # Run the command using subprocess and expect an error to be raised
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.run(command, shell=True, check=True, cwd=os.getcwd())
