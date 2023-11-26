#сделать ещё 5 вар 1 

k = 0
print('здравствуйте, представтесь, пожалуйста')
name = input()
print(name, ', сейчас будет тест!!!', sep = '')
print('Нужно напечатать НОМЕР, подкотором напичатан правельный ответ')

print()
input('если вы готовы нажмите Enter')
print()
print()
print('вопрос №1')
print('2*2 = ?')
print('1)10    2)22   3)3     4)2    5)4')
ans = int(input())
if ans == 5:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()
print('вопрос 2')
print('4! = ?')
print('1)4   2)24    3) 12   4)хз    5)40')
ans = int(input())
if ans == 2:
    print('это правильно')
    k += 1
else:
    print('неправильно')

    
print()
print('вопрос 3')
print('2+2*3-3! = ?')
print('1)2   2)6    3) 3  4)20    5)-2')
ans = int(input())
if ans == 1:
    print('это правильно')
    k += 1
else:
    print('неправильно')

    
print()
print('вопрос 4')
print('реши уравнение: 2х+3х=1х+8 ')
print('1)3   2)2    3)23   4)3    5)4')
ans = int(input())
if ans == 2:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 5')
print('реши уравнение: 2х+3х=-1х+8 ')
print('1)5/7   2)4/3    3)34   4)43   5)5')
ans = int(input())
if ans == 2:
    print('это правильно')
    k += 1
else:
    print('неправильно')

    print()  
print('вопрос 6')
print('реши: 11**2 ')
print('1)3   2)22    3)121   4)1111   5)11')
ans = int(input())
if ans == 3:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 7')
print('раскрой скобки: -2(12+23) ')
print('1)-24-46   2)-24+46   3)24+46   4)23   5)404')
ans = int(input())
if ans == 1:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 8')
print('найди значение выражения: 2x+3x:2*3+1, если x=2 ')
print('1)12   2)13   3)14   4)15   5)2')
ans = int(input())
if ans ==3:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 9')
print('найди значение выражения: 2x+(3x:3*2)+1, если x=0.5')
print('1)2   2)3    3)5   4)1.5   5)4')
ans = int(input())
if ans == 2:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 10')
print('сколько нулей имеет число 25!')
print('1)4   2)5    3)7   4)8   5)6')
ans = int(input())
if ans == 5:
    print('это правильно')
    k += 1
else:
    print('неправильно')
    

if k >= 10*0.85:
    print('ваша оценка 5')
    print('правильных ответов', k)
elif k >= 10*0.7:
    print('ваша оценка 4')
    print('правильных ответов', k)
elif k >= 10*0.5:
    print('ваша оценка 3')
    print('правильных ответов', k)
else:
    print('ваша оценка 2')
    print('правильных ответов', k)

