import os
from pathlib import Path
import shutil
from markdown_blocks import markdown_to_html_node, extract_title

def recursive_file_copy(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            recursive_file_copy(from_path, dest_path)

# def generate_page(from_path, template_path, dest_path):
# 	print(f"Generating page from {from_path} to {dest_path} using {template_path}")

# 	with open(from_path, 'r') as file:
# 		md_str = file.read()

# 	with open(template_path, 'r') as file:
# 		template = file.read()

# 	md_content = markdown_to_html_node(md_str).to_html()
# 	md_title = extract_title(md_str)
# 	filled_template = template.replace("{{ Title }}", md_title)
# 	filled_template = filled_template.replace("{{ Content }}", md_content)

# 	os.makedirs(os.path.dirname(dest_path), exist_ok=True)
# 	with open(dest_path, "w", encoding="utf-8") as f:
# 		f.write(filled_template)

# def generate_pages_recursive(from_path, template_path, dest_path, basepath):
# 	for entry in os.listdir(dir_path_content):
# 		entry_path = os.path.join(dir_path_content, entry)

# 		if os.path.isfile(entry_path):
# 			if entry.endswith('.md'):
# 				dest_filename = entry.replace('.md', '.html')
# 				dest_file_path = os.path.join(dest_dir_path, dest_filename)
# 				generate_page(entry_path, template_path, dest_file_path)
# 		else:
# 			new_dest_dir = os.path.join(dest_dir_path, entry)
# 			os.makedirs(new_dest_dir, exist_ok=True)
# 			generate_pages_recursive(entry_path, template_path, new_dest_dir)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")