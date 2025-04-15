import os
import shutil

from textnode import TextNode, TextType
from copystatic import recursive_file_copy, generate_pages_recursive

def main():
    static_dir = os.path.join(os.getcwd(), "static")
    public_dir = os.path.join(os.getcwd(), "public")

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    recursive_file_copy(static_dir, public_dir)
    generate_pages_recursive("content", "./template.html", "public")

main()
