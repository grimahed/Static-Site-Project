import os
import shutil
import sys
from pathlib import Path
from enum import Enum
from textnode import *
from htmlnode import *
from blocktypes import *

if len(sys.argv) == 2:
    basepath = sys.argv[1]
else:
    basepath = "/"
#extract stuff
def extract_title(markdown):
        blocks = markdown_to_blocks(markdown)
        for block in blocks:
            block_type = block_to_block_type(block)
            if block_type == BlockType.HEADING:
                new_block = block[2:]
                finalized = new_block.strip()
                return finalized
            elif block_type != BlockType.HEADING:
                continue
        raise Exception("no heading to return")

#generate the page
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    
    #from_path stuff
    with open(from_path, "r") as f:
        read_from_file = f.read() #read as in pronounced "red"
    #template path stuff
    with open(template_path, "r") as t:
        read_template_file = t.read() #same here
    
    #getting stuff and making html stuff
    md_html_node = markdown_to_html_node(read_from_file)
    md_html = md_html_node.to_html() #the actual string
    title = extract_title(read_from_file)

    #build thing
    built_html = read_template_file
    built_html2 = built_html.replace("{{ Title }}", title)
    built_html3 = built_html2.replace("{{ Content }}", md_html)
    built_html4 = built_html3.replace('href="/', f'href="{basepath}')
    final_html = built_html4.replace('src="/', f'src="{basepath}')
                                     
    #write the thing
    dirs = os.path.dirname(dest_path)
    os.makedirs(dirs, exist_ok=True)
    with open(dest_path, "w") as d:
        uploaded_html = d.write(final_html)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, baepath):
    for filepath in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filepath)
        dest_path = os.path.join(dest_dir_path, filepath)   
        if os.path.isfile(from_path):
            html_filepath = str(Path(dest_path).with_suffix(".html"))
            page = generate_page(from_path, template_path, html_filepath, basepath)
        elif os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, dest_path, basepath)





def main():
    text = "this is text"
    text_type = TextType.BOLD_TEXT
    url = "https://www.aq.com"
    Sample = TextNode(text, text_type, url)
    print(Sample)

    def rec_copy_stuff(source, dest):
        #delete the entire public directory and create a new one
        if os.path.exists(dest):
            shutil.rmtree(dest)
            os.mkdir(dest)
        else:
            os.mkdir(dest)
        
        #copy everything
        stuff = os.listdir(source)
        for thing in stuff:
            file_path = os.path.join(source, thing)
            dest_path = os.path.join(dest, thing)
            if os.path.isfile(file_path):
                shutil.copy(file_path, dest_path)
            elif os.path.isdir(file_path):
                rec_copy_stuff(file_path, dest_path)
    rec_copy_stuff("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)
    
        


if __name__ == "__main__":
    main()