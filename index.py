import itertools
import PyPDF2
import time


start = time.time()

pdf_file = open("DATIMESE0223.PDF", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)

num_letter = 6
characters = ["g", "o", "A", "L", "5", "9"]

combinations = list(itertools.product(characters, repeat=num_letter))
index = 0
for i in combinations:
    combinations[index] = ''.join(str(x) for x in i)
    index += 1

print("\nInizio decrittazione\n")

found = False

for i in combinations:
    try:
        pdf_reader.decrypt(f"{i}")
        page_content1 = pdf_reader.pages[0].extract_text()
        page_content2 = pdf_reader.pages[1].extract_text()
        password = i
        print(f"La password è: {password}")
        pdf_file.close()
        found = True
        break
    except:
        pass

if found == True:
    print(f"La password è: {password}")
else:
    print("Impossibile decriptare il file\n")

end = time.time()
print("Tempo di esecuzione :", round(end-start, 2), "secondi\n")
