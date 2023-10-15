#!/usr/bin/python3
"""markdown to html script"""


import sys
import os
import markdown


def markdown2html(markdown_file, html_file):
    """script to convert markdown file
    to corresponding html"""
    if not os.path.exists(markdown_file):
        sys.stderr.write("Missing {}\n".format(markdown_file))
        sys.exit(1)

    with open(markdown_file, 'r') as file:
        markdown_text = file.read()

    html_output = markdown.markdown(markdown_text)

    with open(html_file, 'w') as f:
        f.write(html_output)
        f.write("\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    markdown2html(markdown_file, html_file)

    sys.exit(0)
