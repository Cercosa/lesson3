# Вывести последнюю букву в слове
word = 'Arkhangelsk'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Arkhangelsk'
counter = 0
for letter in word.lower():
    if letter == "a":
        counter += 1
print(counter)


# Вывести количество гласных букв в слове
word = 'Arkhangelsk'
vowels = ["a", "e", "i", "o", "u", "y"]
counter = 0
for letter in word.lower():
    if letter in vowels:
        counter += 1
print(counter)


# Вывести количество слов в предложении
sentence = 'We came for a visit'
words = len(sentence.split())
print(words)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'We came for a visit'
separeted_sentence = sentence.split()
for words in separeted_sentence:
    print(words[0])


# Вывести усреднённую длину слова.
sentence = 'We came for a visit'
separated_sentence = sentence.split()
how_many_words = len(separated_sentence)
how_many_letters = 0
for words in separeted_sentence:
    how_many_letters = how_many_letters + len(words) 
avarege = how_many_letters / how_many_words
print(avarege)