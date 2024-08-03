import pdf2image #1.17.0

doc_img = pdf2image.convert_from_path("src/data/doc_nvidia.pdf", dpi=300)

# print one page as example
print("pages:", len(doc_img))
doc_img[35]