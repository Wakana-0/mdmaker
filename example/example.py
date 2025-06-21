from document import MdDocument

md = MdDocument()
md.set_path("output/document.md")
md.headings("Markdown Document Example", level=1)
md.paragraphs("This is an example of a Markdown document generated programmatically.")
md.unordered_list("Item 1")
md.ordered_list(1, "1st item")
md.ordered_list(2, "2nd item")
md.save()