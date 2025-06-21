"""This module handles Markdown document generation."""
import re
import os
from pathlib import Path

__VERSION__ = "0.0.2"
__LICENSE__ = "GPL-3.0"


def enbt(s):
    """
    fill name: extract_number_before_dot
    """
    match = re.match(r'(\d+)\.', s)
    if match:
        return int(match.group(1))
    return None

class MdDocument():
    """
    A class to generate Markdown documents programmatically.
    """
    # ----------init----------
    def __init__(self):
        self.commands = []
    def set_path(self, path):
        """
        Sets the path for the document.
        :param path: The path where the document will be saved.
        """
        self.path = path
    def save(self, path: str = "./output/document.md"):
        """
        Generates the Markdown document and saves it to the specified path.
        :param path: The path where the document will be saved.
        """
        if path is None:
            if hasattr(self, 'path'):
                path = self.path
            else:
                raise ValueError("Path must be specified")

        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.commands))
        print(f"mdmaker: Document saved to {path}")
    #----------init ending----------
    def headings(self, text: str, level: int = 1):
        """
        Adds a heading to the document.
        :param text: The text of the heading.
        :param level: The level of the heading (1-6).
        """
        if level < 1 or level > 6:
            raise ValueError("Heading level must be between 1 and 6")
        self.commands.append(f"{'#' * level} {text}")
    def paragraphs(self, text: str):
        """
        Adds a paragraph to the document.
        """
        self.commands.append(text)
    def unordered_list(self, items: str):
        """
        Starts an unordered list.
        """
        self.commands.append(f"- {items}")
    def ordered_list(self, num: int, items: str):
        """
        Starts an ordered list.
        """
        if num == 1 or enbt(self.commands[-1])+1 == num:
            self.commands.append(f"{num}. {items}")
        else:
            print(self.commands)
            raise ValueError("Ordered list must be sequential")

    def inline_code(self, code: str):
        """
        Adds inline code to the document.
        """
        self.commands.append(f"`{code}`")
    def code_block(self, code: str, laugage: str = None):
        """
        Adds a code block to the document.
        """
        self.commands.append(f"```{laugage}\n{code}\n```")
    def links(self, link_text: str, url: str):
        """
        Adds a link to the document.
        """
        self.commands.append(f"[{link_text}]({url})")
    def line_breaks(self):
        """
        Adds a line break to the document.
        """
        self.commands.append("<br>")
    def strikethrough(self, text: str):
        """
        Adds strikethrough text to the document.
        """
        self.commands.append(f"~~{text}~~")
    def blockquotes(self, text: str):
        """
        Adds a blockquote to the document.
        """
        self.commands.append(f"> {text}")

    def tasklists(self, test: str, checked: bool = False):
        """
        Adds a task list item to the document.
        :param text: The text of the task list item.
        :param checked: Whether the task is checked or not.
        """
        status = "[x]" if checked else "[ ]"
        self.commands.append(f"- {status} {test}")
    def images(self, images_text: str, url: str):
        """
        Adds an image to the document.
        """
        self.commands.append(f"![{images_text}]({url})")
    def escapingc_haracters(self, text: str):
        """
        Escapes special Markdown characters in the text.
        """
        escape_chars = r'\`*_{}[]()#+-.!'
        escaped_text = ''.join(f'\\{char}' if char in escape_chars else char for char in text)
        self.commands.append(escaped_text)
