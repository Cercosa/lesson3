
from collections import Counter
with open('referat.txt', 'r', encoding='utf-8') as f:

    for caracter in f:
        caracter = caracter.replace("\n", "")
        number_characters_string = len(caracter.join(caracter.strip() for caracter in f))
        print(number_characters_string)

with open('referat.txt', 'r', encoding='utf-8') as f:
    text = f.read() 
    file_list = text.split(" ")
    words = len(file_list)
    print(words)

with open('referat.txt', 'r', encoding='utf-8') as f_read:
    with open('referat_new.txt', 'w', encoding='utf-8') as f_write:
        read_text = f_read.read()
        for caracter in read_text:
           caracter = caracter.replace(".", "!")
           print(caracter)
           f_write.write(caracter)   