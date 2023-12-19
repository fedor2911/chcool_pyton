k = 0
print('здравствуйте, представтесь, пожалуйста')
name = input()
print(name, ', сейчас будет тест!!!', sep = '')
print('Нужно напечатать ответ')

print()
input('если вы готовы нажмите Enter')
print()
print()
print('вопрос №1')
print('2*2 = ?')
ans = int(input())
if ans == 4:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()
print('вопрос 2')
print('4! = ?')
ans = int(input())
if ans == 24:
    print('это правильно')
    k += 1
else:
    print('неправильно')

    
print()
print('вопрос 3')
print('2+2*3-3! = ?')
ans = int(input())
if ans == 2:
    print('это правильно')
    k += 1
else:
    print('неправильно')

    
print()
print('вопрос 4')
print('реши уравнение: 2х+3х=1х+8 ')
ans = int(input())
if ans == 2:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 5')
print('реши уравнение: 2х+3х=-1х+8 (ответ введите в неправильной дроби)' )
ans = input()
if ans == '4/3':
    print('это правильно')
    k += 1
else:
    print('неправильно')

    print()  
print('вопрос 6')
print('реши: 11**2 ')
ans = int(input())
if ans == 121:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 7')
print('раскрой скобки: -2(12+23) ')
ans = input()
if ans == '-24-46':
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 8')
print('найди значение выражения: 2x+3x:2*3+1, если x=2 ')
ans = int(input())
if ans == 14:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 9')
print('найди значение выражения: 2x+(3x:3*2)+1, если x=0.5')
ans = int(input())
if ans == 3:
    print('это правильно')
    k += 1
else:
    print('неправильно')

print()  
print('вопрос 10')
print('сколько нулей имеет число 10!')
ans = int(input())
if ans == 2:
    print('это правильно')
    k += 1
else:
    print('неправильно, факториал 10 = 3 628 800, то  есть 1*2*3*4*5*6*7*8*9*10, 4*5*10 дают 2 нуля')
    

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