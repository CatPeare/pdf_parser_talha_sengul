import os
import pypdf
import re # self note: don't forget to try re in case script doesn't work without re

# change folder path with the path wherever your pdfs exists.
folder = r"C:\Users\Talha\Desktop\fff"

find_this_text = input("\n\nPlease paste what you seek, may the force be with you\n\n")

for filename in os.listdir(folder):
    if filename.endswith(".pdf"):
        pdf_file_path = os.path.join(folder, filename)   
        with open(pdf_file_path, "rb") as pdf:
            reader = pypdf.PdfReader(pdf)
            text = ""
            zero = 0
            for page in reader.pages:
                zero += 1
                text += page.extract_text() + "\n"
                if find_this_text in text:
                    print(f"\n\n{filename} contains {len(reader.pages)} pages.\n\nAnd what you seek is in page {zero}.\n\n")
                    break
