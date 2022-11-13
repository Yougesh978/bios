f = lambda x: print("leap year" if ((x%400==0) or (x%100!=0) and (x%4==0)) else 'not leap year')
f(2000)
