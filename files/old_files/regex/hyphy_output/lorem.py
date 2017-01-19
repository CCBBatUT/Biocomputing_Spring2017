import loremipsum
from random import randint

# Define variables used to generate files
num_files = 20     # Number of files 
min_length = 2     # Minimum number of lines per file
max_length = 150   # Maximum number of lines per file

for i in range(num_files):
    
    file_name = "file" + str(i + 1) + ".txt"
    file_size = randint(min_length, max_length)
    sentences = "\n".join(loremipsum.get_sentences(file_size))
    with open(file_name, "w") as f:
        f.write(sentences)