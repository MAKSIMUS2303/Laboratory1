a=int(input('Введите коэффицент a:'))
b=int(input('Введите коэффицент b:'))
c=int(input('Введите коэффицент c:'))
Dis=b**2-4*a*c
if Dis<0:
    print('нет корней')
if Dis==0:
    print(-b/2*a)
if Dis>0:
    x1=(-b+(Dis)**1/2)/2*a
    x2=(-b-(Dis)**1/2)/2*a
    print('Ответ:',x1,',',x2)

