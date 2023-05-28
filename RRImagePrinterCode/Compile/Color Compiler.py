#V: Laku_2023_05_08
try:
    from PIL import Image
    import os
    import sys
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    print('One or more moduels not found')
    input()
    exit()

lis=[]
Path = os.path.join(os.getcwd().replace("\\Compile", ""), "Data/CustomColors")


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

from tkinter import filedialog
imgfile =filedialog.askopenfilename()

print("choose image")
fileName =  imgfile


try: 
    img = Image.open(fileName)
except:
    print('image not found. Make sure you typed file name correctly and the file is in the images folder')
    input()
    exit()
print("Image obtained.")
try:
    Min= int(input('Auto remove colors that appear in the image less then the input number:\n'))
except:
    print('not a number')
    input()
    exit()
while True:
    inpu=input('Please input a number that will be the min diffrence between color. \nRecommended "20".\n')
    if inpu=='':
        inpu=20
    try:
        divider=int(inpu)
        break
    except:
        print('Error: Please input a whole number')

    
img = img.convert("RGBA")
with open(Path, 'a') as col:
    pass
with open(Path, 'w') as col:
    print('Collecting colors. This may take a little time.')
    

    [width,height] = img.size
    colList=[]
    amountlist= []
    text='(1,1,1). 9999999999 .#000000. Do not remove this color\n(255,255,255). 9999999999 .#FFFFFF. Do not remove this color\n'
    removed=[]
    for x in range(0,int(width)):
        for y in range(0, height):
            CurrentColor = img.getpixel((x,y))
            if CurrentColor[3] == 0:
                continue
            

            else:
                n1=round(CurrentColor[0]/divider)*divider
                if n1>255:
                    n1=255
                n2=round(CurrentColor[1]/divider)*divider
                if n2>255:
                    n2=255
                n3=round(CurrentColor[2]/divider)*divider
                if n3>255:
                    n3=255
                Current= (n1,n2,n3)
            if Current[0]<2 and Current[1]<2 and Current[2]<2:
                continue
            if Current[0]>254 and Current[1]>254 and Current[2]>254:
                continue
            
            if Current in colList:
                index=colList.index(Current)
                amountlist[index] += 1
            else:
                colList.append(Current)
                amountlist.append(1)

    for i in range(0,len(colList)):
        if amountlist[i] < Min:
            
            removed.append(colList[i])
        else:
            text +=f'{colList[i]}.    {amountlist[i]}    .{rgb_to_hex(colList[i][0],colList[i][1],colList[i][2])}\n'
    while len(removed)>0:
        del amountlist[colList.index(removed[0])]
        del colList[colList.index(removed[0])]
        del removed[0]
    col.write(text)
    print('Prosess finished. Colors found:' + str(len(colList)+2))
    
    print('Estimated time for importing ' + str((len(colList)*6.5)/60) + ' minutes')
    input()
    

    

            
