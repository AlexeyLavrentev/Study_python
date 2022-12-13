# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def delete_word(word, text):
    text_list = text.split(' ')
    count = 0
    res = ''
    res_list = []
    check = 0
    for word in text_list:
        for letter in range(len(word)):
            if (word[letter] == 'а') and (word[letter + 1] == 'б') and (word[letter + 2] == 'в'):
                check = 1
                break
        if check == 0:
            res_list.append(word)
        else:
            check = 0

    for i in res_list:
        res += i + ' '

    return res


r = open('text.txt', 'r', encoding='utf-8')
values = r.readlines()
r.close()
value = values[0]
print(f'Из файла импортируем текст: \n{value}\n')
word = 'абв'

result = delete_word(word, value)
print(f'Из текста удалили все слова с "{word}". Результат: \n{result}')