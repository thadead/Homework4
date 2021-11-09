a = input()
b = input()
start = -1
summ = 0
bindex  = ''
while True:
    start = a.find(b, start+1)
    if start == -1:
        break
    summ += 1
    bindex = bindex + str(start) + ' '
print('Индексы символо b в строке a: ', bindex)
print('Всего символов b в строке a: ', summ)