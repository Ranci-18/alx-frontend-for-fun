#!/usr/bin/python3
"""markdown to html script"""
import sys
import os
import markdown


def markdown2html(markdown_file, html_file):
    """script to convert markdown file
    to corresponding html"""
    # Check if the markdown file exists in the current directory
    if not os.path.exists(markdown_file):
        sys.stderr.write("Missing {}\n".format(markdown_file))
        sys.exit(1)

    # Read the contents of the markdown file
    with open(markdown_file, mode='r', encoding='utf-8') as file:
        markdown_text = file.read()

    # Convert the contents to html
    html_output = markdown.markdown(markdown_text)

    # Then write the html content to the html file
    with open(html_file, mode='w', encoding='utf-8') as f:
        f.write(html_output)
        f.write("\n")


if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    # Extract the markdown and html files from the command-line
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Perform the conversion
    markdown2html(markdown_file, html_file)

    sys.exit(0)
