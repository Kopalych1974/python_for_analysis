'''
Задание дополнительное

Задание 1
https://ru.wikipedia.org/wiki/Fizz_buzz
Начинающий произносит число “1”, и каждый следующий игрок прибавляет к предыдущему значению единицу. Когда число делится на три оно заменяется на fizz, если число делится на пять, то произносится buzz. Числа, делящиеся на три и пять одновременно заменяются на fizz buzz. Сделавший ошибку игрок исключается из игры.

Типичная партия в fizz buzz выглядит так:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, …

Напишите код, выводящий на экран первые n элементов этой игры (естественно, корректные).
'''


count = 1
elements_to_print = int(input('How many elements to print?'))

while count <= elements_to_show:
    if count % 3 == count % 5 == 0:
        print('Fizz Buzz')
    elif count % 3 == 0:
        print('Fizz')
    elif count % 5 ==0:
        print('Buzz')
    else:
        print(count)
    count += 1

'''
Задание 2
Датчик принимает сигнал, состоящий из 0 и 1. Известно, что сигнал имеет периодичность, не превышающей натурального числа n. Напишите код, который вычисляет периодичность сигнала. Считайте, что 3 < n < 1000, а общая длина сигнала значительно превышает n.

Пример сигнала с периодичностью 4 (повторяющийся элемент 1011):
1011101110111011101110111011101110111011

Еще одна интерпретация задачи, но без кода: https://tproger.ru/problems/endless-train/

'''


signal = input('Receiving a signal... ')
print('Received signal is ', signal)

for i in range(1, len(signal)):
    element = signal[:i]
    if signal.count(element) == len(signal)/i:
        print('Element is ', element, ' with ', signal.count(element), ' repetitions in signal')
        break


'''
Задание 3
Дано слово из латинских букв. Напишите скрипт, который выводит на экран букву из середины слова (если число букв нечетное). Если букв четное число, то на экран выводятся две буквы из середины.

Для ‘test’ - 'es’
Для ‘testing’ - ‘t’

'''


word = input('Write a word ')
lenght = len(word)
if lenght % 2 == 0:
    print(word[lenght//2-1:lenght//2+1])
else:
    print(word[lenght//2])
    
