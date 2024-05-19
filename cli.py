import argparse
from pdf_parser.core import PDFParser

def main():
    """
    Command-line interface to parse PDF content and write it to a text file
    """
    # Create argument parser
    parser = argparse.ArgumentParser(description="Parse PDF content to text file.")

    # Add argument for the path to the PDF file
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file.")

    # Add optional argument for the parsed file path
    parser.add_argument(
        "-o",
        "--parsed_file_path",
        type=str,
        help="Path to the parsed text file. If not specified, the parsed file will have the same name as the PDF file with '_cli_parsed.txt' appended.",
    )

    # Parse the command-line arguments provided
    args = parser.parse_args()

    # Create PDFParser instance
    pdf_parser = PDFParser(args.pdf_path)

    # If parsed_file_path is not provided, use the default parsed file path
    if not args.parsed_file_path:
        default_parsed_file_path = f"{args.pdf_path[:-4]}_cli_parsed.txt"
        pdf_parser.parse_to_file(default_parsed_file_path)
    else:
        pdf_parser.parse_to_file(args.parsed_file_path)

if __name__ == "__main__":
    # If the script is executed directly, run the main function
    main()
