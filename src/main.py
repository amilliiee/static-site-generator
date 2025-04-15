import os
import shutil
import sys

from copystatic import recursive_file_copy, generate_pages_recursive

def main():
    static_dir = "./static"
    public_dir = "./docs"
    content_dir = "./content"
    template_path = "./template.html"
    
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        
    recursive_file_copy(static_dir, public_dir)
    generate_pages_recursive(content_dir, template_path, public_dir, basepath)
    

    # if os.path.exists(public_dir):
    #     shutil.rmtree(public_dir)

    # recursive_file_copy(static_dir, public_dir)
    # generate_pages_recursive("content", "./template.html", "public")

main()
