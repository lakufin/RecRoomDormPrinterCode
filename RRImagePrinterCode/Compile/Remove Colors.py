#V: Laku_2023_05_08
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

Path = os.path.join(os.getcwd().replace("\\Compile", ""), "Data/CustomColors")

try:
    open(Path)
except:
    print('Color file not found')
    input()
    exit()
print('File found. ')
try:
    nput=int(input('Reduce to how many colors\n'))
except:
    print('Not a number')
    input()
    exit()
lista=[]
a=1
with open(Path, 'r') as file:
    for i in file:
        if a > 2:
            lista.append(str(i))

        a+=1
    
while len(lista)+2>nput:
    pienin=0
    amount=999999999999999999999
    for p in lista:
        if  amount> int((p.split('.'))[1]):
            pienin=lista.index(p)
            amount=int((p.split('.'))[1])
    del lista[pienin]

text='(1,1,1). 9999999999 .#000000. Do not remove this color\n(255,255,255). 9999999999 .#FFFFFF. Do not remove this color\n'
for o in lista:
    text+=o
print('finished')
with open(Path, 'w') as file2:
    file2.write(text)
