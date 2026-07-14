import fitz

pdf = fitz.open("CL_DAV_Rules.pdf")

print(f"Your PDF has {len(pdf)} pages")

#to get each 
# for page_number in range(len(pdf)):
#     page=pdf[page_number]

#     text=page.get_text()

#     print(f"Page {page_number+1} Content : ")
#     print(text)

# text="himanshu sharma is a software development intern at idea foundation, a company est. in 2009 "

full_text=""
for page_number in range(len(pdf)):
    page=pdf[page_number]
    text=page.get_text()

    full_text+=text 
    
chunks=[]
chunk_size=500

for i in range(0, len(full_text),chunk_size):
    chunk=full_text[i:i+chunk_size]

    chunks.append(chunk)



print(chunks)












#to split word-wise we would have done this
# clean_text = text.split()

#for space separated chunks
# chunk_size=10
# chunks=[]

# for i in range(0,len(text),chunk_size):
#     chunks= text.split(" ")

# for i in range(len(chunks)):
#     print(chunks[i])