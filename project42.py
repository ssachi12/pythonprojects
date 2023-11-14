from pypdf import PdfReader
import pdfplumber
reader = PdfReader("file.pdf")

# Print the number of pages in the PDF
print(f"There are {len(reader.pages)} Pages")

# Get the first page (index 0)
page = reader.pages[0]
# Use extract_text() to get the text of the page
print(page.extract_text())

# Go through every page and get the text
for i in range(len(reader.pages)):
  page = reader.pages[i]
  print(page.extract_text())


# The import name for this library is fitz
import fitz

# Create a document object
doc = fitz.open('file.pdf')  # or fitz.Document(filename)

# Extract the number of pages (int)
print(doc.page_count)

# the metadata (dict) e.g., the author,...
print(doc.metadata)

# Get the page by their index
page = doc.load_page(0)
 # or page = doc[0]

# read a Page
text = page.get_text()
print(text)

# Render and save the page as an image
pix = page.get_pixmap()
pix.save(f"page-{page.number}.png")

# get all links on a page
links = page.get_links()
print(links)

# Render and save all the pages as images
for i in range(doc.page_count):
  page = doc.load_page(i)
  pix = page.get_pixmap()
  pix.save("page-%i.png" % page.number)

# get the links on all pages
for i in range(doc.page_count):
  page = doc.load_page(i)
  link = page.get_links()
  print(link)


with pdfplumber.open('example.pdf') as pdf:
    # iterate over each page
    for page in pdf.pages:
        # extract text
        text = page.extract_text()
        print(text)

