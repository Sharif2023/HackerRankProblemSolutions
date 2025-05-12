for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((pow(10,i)//9)*i)

"""
Explaination:
N=5
i=1------------->N-1
1*1=1
11*2=22
111*3=333
1111*4=444

[pow(10*i)//9]*i

simulation:
i=1, 10^1=10/9=1*1=1
i=2, 10^2=100/9=11*2=22
i=3, 10^3=1000/9=111*3=333
i=4, 10^4=10000/9=1111*4=4444
"""
