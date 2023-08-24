word = str(input('Введите слово для проверки: '))
word_reverse = word[::-1]

if word == word_reverse:
    print(True)
else:
    print(False)